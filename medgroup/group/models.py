from django.db import models
from datetime import datetime
# Create your models here.

class Register(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    username=models.CharField(max_length=50,unique=True)
    email=models.EmailField()
    ph_no=models.CharField(max_length=10,unique=True)
    password=models.CharField(max_length=1000,default="")
    image_link=models.CharField(max_length=100,default="")

    def __str__(self):
        return f'{self.first_name},{self.last_name},{self.username}'

class Chat(models.Model):
    chats=models.CharField(max_length=1000)
    time=models.DateTimeField(default=datetime.now)
    user=models.CharField(max_length=100)
    channel=models.CharField(max_length=100)
    def __str__(self):
        return f'{self.time}'

class Channels(models.Model):
    user=models.CharField(max_length=100)
    channel=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.channel}'
