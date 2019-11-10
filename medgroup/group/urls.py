from django.urls import path
from . import views

urlpatterns=[
     path('',views.index,name='home'),
     path('register',views.Signup,name='register'),
     path('login',views.Login,name='login'),
     path('userpage/<user>',views.dashboard,name='dashboard'),
]
