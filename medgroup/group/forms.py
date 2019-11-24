from django.forms import forms,CharField,EmailField,PasswordInput
from group.models import Register
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from hashing import *



class SignupForm(forms.Form):
    first_name=CharField(max_length=100,label='First Name')
    last_name=CharField(max_length=100,label='Last Name')
    username=CharField(max_length=10,label='Username',help_text='Create your unique username')
    email=EmailField()
    password=CharField(widget=PasswordInput,max_length=12,help_text='Create your password')
    cnf_pass=CharField(widget=PasswordInput,max_length=12,label='confirm password')
    ph=CharField(max_length=10,label='Phone No',help_text='enter your phone no')

    def clean_username(self):
        us=self.cleaned_data['username']
        if Register.objects.filter(username=us).exists():
            raise ValidationError(_(" the given user name is taken "))
        return us
    def clean_email(self):
        em=self.cleaned_data['email']
        if Register.objects.filter(email=em).exists():
            raise ValidationError(_("The given email is already registered"))
        return em
    def clean_cnf_pass(self):
        ps=self.cleaned_data['password']
        cnf=self.cleaned_data['cnf_pass']

        if len(ps)<6:
            raise ValidationError(_("Password must be atleast 8 char long"))
        if  ps!=cnf:
            raise ValidationError(_("please reconfirm your password"))
        return cnf
    def clean_ph(self):
        em=self.cleaned_data['ph']
        if Register.objects.filter(ph_no=em).exists():
            raise ValidationError(_("The given number is already registered"))
        return em

class LoginForm(forms.Form):
    username=CharField(max_length=10,label='Username')
    password=CharField(max_length=12,label='Password',widget=PasswordInput)


    def clean_password(self):
        us=self.cleaned_data['username']
        ps=self.cleaned_data['password']
        if Register.objects.filter(username=us).exists():
            pass
        else:
            raise ValidationError(_("User name not registered"))
            return us

        actual=Register.objects.get(username=us).password
        if verify_password(actual,ps) is False:
            raise ValidationError(_("Inavlid Password"))
        return ps


class VerificationForm(forms.Form):
    code=CharField(max_length=4,help_text="enter the opt sent ",label="Otp")



## TODO: update form ... fields not clear


class ForgotPassForm(forms.Form):
    email=EmailField()

    def clean_email(self):
        us=self.cleaned_data['email']
        if Register.objects.filter(email=us).exists():
            print(Register.objects.filter(email=us))
            return us
        else:
            raise ValidationError(_("Sorry that email is not registered with us !! Try signup "))
        return us


class ResetPassForm(forms.Form):
    password=CharField(widget=PasswordInput(),max_length=12,label="new password")
    confirm=CharField(widget=PasswordInput(),max_length=12,label="Confirm password")

    def clean_confirm(self):
        pas=self.cleaned_data['password']
        cnf=self.cleaned_data['confirm']

        if len(pas)<6:
            raise ValidationError(_("Minimum 6 characters required"))

        if pas!=cnf:
            raise ValidationError(_("Please reconfirm your password"))
        return pas


class NewChannelForm(forms.Form):
    """Creatig forms for new channel"""
    room_name=CharField(max_length=100,label="Channel Name")
    Creator=CharField(max_length=100,label="Username")
    motto =CharField(max_length=100,label="Objective",help_text="Enter your objective of creating channel")



class UpdateForm(forms.Form):
    """docstring for UpdateForm.forms.Form
         def __init__(self, arg):"""
    first_name=CharField(max_length=100,label="First Name")
    last_name=CharField(max_length=100,label="Last Name")
    email=CharField(max_length=100,label="Email")

    
