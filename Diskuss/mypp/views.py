from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse,JsonResponse,HttpResponseNotFound

# Create your views here.





def profile(request):
    
    return render(request,'profile.html')

def questionupload(request):
    
    return render(request,'QuestionUpload.html')

def results(request):
    
    return render(request,'result.html')


def studentHome(request):
    
    return render(request,'SHome.html')

def solution(request):
    
    return render(request,'solutionpage.html')

def solutionSubmit(request):
    
    return render(request,'solutionSubmit.html')

def sResults(request):
    
    return render(request,'SResults.html')


def sSolutionSubmit(request):
    
    return render(request,'SSolutionSubmit.html')



def index(request):
    
    return render(request,'index.html')



def signout(request):
    auth.logout(request)
    return redirect('/')



def home(request):
    
    return render(request,'Home.html')

def homepage(request):
    
    return render(request,'homepage.html')

def shop(request):
    return render(request,'shop.html')

#def sign_up(request):
    #return render(request,'sign-up.html')

def counter(request):
    
    email=request.POST['email']
    passw=request.POST['psw']
    details={
        'id':email,
        'password':passw 
    }
    return render(request,'counter.html',details)




def signup(request):


    data=open('data.txt','a')
    if request.method=='POST':
        name=request.POST['name']
        
        username=request.POST['username']
        email=request.POST['email']
        
        password1=request.POST['password1']
        password2=request.POST['password2']
        address=request.POST['address']
        
        data.write(name+"  "+username+"  "+password1+"  "+address+"\n")

        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Exits')
                return redirect('signup',{'msg':'Email already exists'})
            
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Exits')
                return redirect('signup',{'msg':'username already'})
            else:
                
                
                user=User.objects.create_user(username=username,email=email,password=password1)
                #createDatabase(username=username,address=acc[0],privateKey=acc[1],password=password1)
                user.save()
                #accounts(username,password1)
                #messages.info("Signup Complete !  Login Now")
                return redirect('signin')
        
        else:
            #messages.info("Passwords not same")  
            return redirect ('signup',{'msg':'Password not same'})
    else:
        return render(request,'signup.html')  


def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('profile')
        else:
            return redirect ('signin') 
            #messages.info("Incorrect Password")
            
        
        
    else:

        return render(request,'signin.html')
