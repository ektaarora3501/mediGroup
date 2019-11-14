from django.urls import path
from . import views

urlpatterns=[
     path('',views.index,name='home'),
     path('register',views.Signup,name='register'),
     path('send_mail/<phone>',views.Send,name='send_verifi_ph'),
     path('verify_phone/<code>/<phone>',views.verify_ph,name='verify_phone'),
     path('login',views.Login,name='login'),
     path('forgot_pass',views.forgot_pass,name='forgot_pass'),
     path('userpage/<user>',views.dashboard,name='dashboard'),
     path('logout/<user>',views.logout,name='logout'),
]
