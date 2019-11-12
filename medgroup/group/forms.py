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

class LoginForm(forms.Form):
    username=CharField(max_length=10,label='Username')
    password=CharField(max_length=12,label='Password',widget=PasswordInput)

    def clean_username(self):
        us=self.cleaned_data['username']
        if Register.objects.filter(username=us).exists():
            return us
        else:
            raise ValidationError(_("The given username not registered"))
    def clean_password(self):
        us=self.cleaned_data['username']
        ps=self.cleaned_data['password']
        actual=Register.objects.get(username=us).password
        if verify_password(actual,ps) is False:
            raise ValidationError(_("Inavlid Password"))
        return ps
