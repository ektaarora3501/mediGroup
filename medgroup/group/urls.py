from django.urls import path
from . import views

urlpatterns=[
     path('',views.index,name='home'),
     path('register',views.Signup,name='register'),
     path('send_mail/<phone>',views.Send,name='send_verifi_ph'),
     path('verify_phone/<code>/<phone>',views.verify_ph,name='verify_phone'),
     path('login',views.Login,name='login'),
     path('reset/<code1>/<id>/<code2>',views.Reset,name='reset_pass'),
     path('forgot_pass',views.forgot_pass,name='forgot_pass'),
     path('join/<str:room_name>',views.Join_room,name='join_room'),
     path('channel_create',views.Channel_create,name='create_channel'),
     path('userpage/<user>',views.dashboard,name='dashboard'),
     path('chat/<str:room_name>/',views.room,name='room'),
     path('logout/<user>',views.Logout,name='logout'),
]
