from django.db import models
from datetime import datetime
from django.conf import settings
from django.urls import reverse
from .validators import validate_category
from django.db.models.signals import pre_save, post_save
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
    
    @property
    def title(self):
        return self.username

class Chat(models.Model):
    chats=models.CharField(max_length=1000)
    time=models.DateTimeField(default=datetime.now)
    user=models.CharField(max_length=100)
    channel=models.CharField(max_length=100)
    def __str__(self):
        return f'{self.time},{self.chats},{self.channel},{self.user}'

#database for new channels and storing their creator_names
class Channels(models.Model):
    creator=models.CharField(max_length=100)
    channel=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return f'{self.channel}'

# a database for all the users connected to any channel
class Members(models.Model):
    member=models.CharField(max_length=100)
    channel=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.member},{self.channel}'


