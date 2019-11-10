from django.db import models

# Create your models here.

class Register(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    username=models.CharField(max_length=50,unique=True)
    email=models.EmailField()
    ph_no=models.CharField(max_length=10)
    password=models.CharField(max_length=1000,default="")

    def __str__(self):
        return f'{self.first_name},{self.last_name},{self.username}'
