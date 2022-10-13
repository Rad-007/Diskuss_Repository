from django import urls
from django.urls import path , include
from . import views

from django.conf import settings #add this
from django.conf.urls.static import static #add this
#from inqu.views import CreateCheckoutSessionView
from django.conf.urls import url

from django.views.static import serve

urlpatterns=[
    #path('admin/',admin.site.urls),
    path('',views.homepage,name='homepage'),
    path('shop',views.shop,name='shop'),
    path('home',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('results',views.results,name='results'),
    path('questionupload',views.questionupload,name='questionupload'),
    path('studentHome',views.studentHome,name='studentHome'),
    path('solution',views.solution,name='solution'),
    path('solutionSubmit',views.solutionSubmit,name='solutionSubmit'),
    path('sResults',views.sResults,name='sResults'),
    path('sSolutionSubmit',views.sSolutionSubmit,name='sSolutionSubmit'),
    path('index',views.index,name='index'),


    #path('', views.sign_in ,name='sign_in'),
    #path('counter',views.counter ,name='counter')
    #path('', views.sign_up ,name='sign_up'),
   
]