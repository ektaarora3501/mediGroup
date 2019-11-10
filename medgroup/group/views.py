from django.shortcuts import render,redirect
from group.models import Register
from django.urls import reverse,reverse_lazy
from group.forms import SignupForm,LoginForm
from django.http import HttpResponseRedirect
from hashing import *
# Create your views here.


def index(request):
    return render(request,'index.html')

def Signup(request):
    if request.method=='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            us=Register()
            us.first_name=form.cleaned_data['first_name']
            us.last_name=form.cleaned_data['last_name']
            us.username=form.cleaned_data['username']
            us.email=form.cleaned_data['email']
            ps=form.cleaned_data['password']
            us.password=hash_password(ps)
            us.ph_no=form.cleaned_data['ph']
            print(us.password)
            us.save()

            return HttpResponseRedirect(reverse('login'))

    else:
         form=SignupForm()
    context={
         'form':form,
         }
    return render(request,'Signup.html',context)



def Login(request):
    if request.method=="POST":
        form=LoginForm(request.POST)

        if form.is_valid():
           # # TODO: add on to verify user
           username=form.cleaned_data['username']
           return HttpResponseRedirect(reverse('dashboard',args=(username,)))

    else:
        form=LoginForm()
    context={
    'form':form,
    }
    return render(request,'Login.html',context)


def dashboard(request,user):
    context={
    'user':user
    }

    return render(request,'dashboard.html',context=context)
