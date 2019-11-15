from django.shortcuts import render,redirect
from group.models import Register
from django.urls import reverse,reverse_lazy
from group.forms import SignupForm,LoginForm,VerificationForm,ForgotPassForm
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from hashing import *
import random
import os
from twilio.rest import Client
from django.core.mail import EmailMessage
# Create your views here.

account_sid="**************************"
auth_token="*****************************"

client=Client(account_sid,auth_token)


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
            return HttpResponseRedirect(reverse('send_verifi_ph',args=(us.ph_no,)))

    else:
        form=SignupForm()
    context={
         'form':form,
         }
    return render(request,'Signup.html',context)


def Send(request,phone):
    v=str(random.randrange(1000,9999))
    value=hash_password(v)
    st='here is your otp'+v
    try:
        message = client.messages.create(
                                  body=st,
                                  from_='whatsapp:+14155238886',
                                  to='whatsapp:****************'
                              )
        print("otp sent")
    except:
        print("error in sending message")

    return HttpResponseRedirect(reverse('verify_phone',args=(value,phone)))






def Login(request):
    if request.session.get('name'):
       nm=request.session.get('name')
       return HttpResponseRedirect(reverse('dashboard',args=(nm,)))
    else:
       if request.method=="POST":
           form=LoginForm(request.POST)

           if form.is_valid():
              username=form.cleaned_data['username']
              request.session['name']=username
              print(request.session['name'])
              print("sesssion set!")
              return HttpResponseRedirect(reverse('dashboard',args=(username,)))
       else:
            form=LoginForm()
       context={
             'form':form,
         }
       return render(request,'Login.html',context)


def dashboard(request,user):
    if request.session.get('name')==user:
        us=Register.objects.get(username=user)
        if request.method == 'POST' :
            if request.FILES['myfile']:
                myfile = request.FILES['myfile']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)
                us.img_link=uploaded_file_url
                us.save()
                print(uploaded_file_url)
                return render(request, 'dashboard.html', {
                    'us':us,'user':user,
                    })
        context={
        'user':user
        }
        return render(request,'dashboard.html',context=context)

    else:
        return HttpResponseRedirect(reverse('login'))


def verify_ph(request,code,phone):
#    print(phone,code)
    err=None
    if request.method=='POST':
        form = VerificationForm(request.POST)
        if form.is_valid():
            username=Register.objects.get(ph_no=phone).username
            data=form.cleaned_data['code']
            request.session['name']=username
            if(verify_password(code,data) is True):
                return HttpResponseRedirect(reverse('dashboard',args=(username,)))
            else:
                err="invalid otp"
                context={
                     'err':err,
                     'ph':phone,
                     'form':form,
                     }
                return render(request,'verify.html',context)

    else:
        form=VerificationForm()
        context={
         'err':err,
         'ph':phone,
         'form':form,
         }
        return render(request,'verify.html',context)



def forgot_pass(request):
    err="please enter the email assosiated, We will check and send to reset password link soon"
    if request.method=='POST':
        form = ForgotPassForm(request.POST)
        if form.is_valid():
            print("here ,form valid ")
            msg = EmailMessage('Email Setup link',
                        to=['*****************@gmail.com'])
            msg.send()
            print("mail sent")
            # TODO:  set up email link and update password
            return HttpResponseRedirect(reverse('login'))
        else:
            err =" email not registered "
            context={
             'err':err,
             'form':form,
             }

            return render(request,'forgot_pass.html',context)

    else:
        form=ForgotPassForm()
        context={
         'err':err,
         'form':form,
         }

        return render(request,'forgot_pass.html',context)



def logout(request,user):
    try:
        del request.session['name']
        print("user deleted")
        print(request.session['name'])
    except :
          pass
    return HttpResponseRedirect(reverse('login'))
