from django.shortcuts import render,redirect
from group.models import Register,Channels,Chat,Members
from django.urls import reverse,reverse_lazy
from group.forms import SignupForm,LoginForm,VerificationForm,ForgotPassForm,ResetPassForm
from django.http import HttpResponseRedirect
from django.utils.safestring import mark_safe
from django.core.files.storage import FileSystemStorage
from twilio.rest import Client
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from hashing import *
import random
import os
import json
# Create your views here.

account_sid="***************************"
auth_token="++++++++++++++++++++++++++"

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
                                  from_='whatsapp:+****************',
                                  to='whatsapp:***********')
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
        ch=Members.objects.filter(member=user).values_list('channel', flat=True).order_by('id')
        print(ch)
        all_ch=Channels.objects.all().values_list('channel', flat=True).order_by('id')
        print(all_ch)
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
                    'us':us,'user':user,'ch':ch,'all':all_ch,
                    })
        context={
        'user':user,
        'ch':ch,
        'all':all_ch,

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
            email=form.cleaned_data['email']
            us=str(Register.objects.get(email=email).id)
            print(us)
            rn=str(random.randrange(1000,9999))
            code1=hash_password(rn)
            code2=hash_password(rn)
            email_link=str('http://127.0.0.1:8000/medico/reset/'+code1+'/'+us + '/' +code2)
            subject, from_email, to = 'hello', '+++++++++++@gmail.com', '************@gmail.com'
            text_content = 'This is an important message.'
            html_content = 'someone  requested reset password for your account ,click on the link below <br>'+email_link
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
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



def Logout(request,user):
    try:
        del request.session['name']
        print("user deleted")
        print(request.session['name'])
    except :
          pass
    return HttpResponseRedirect(reverse('login'))


def Reset(request,code1,id,code2):
    print(id)
    us=Register.objects.get(id=id)
    if request.method=='POST':
        form = ResetPassForm(request.POST)
        if form.is_valid():
            password=form.cleaned_data['password']
            print("saved",password)
            ps=hash_password(password)
            us.password=ps
            us.save()
            return HttpResponseRedirect(reverse('login'))

    else:
        form=ResetPassForm()
    context={
         'username':us.username,
         'form':form,
         }
    return render(request,'set_pass.html',context)


def room(request, room_name):
    if request.session.get('name'):
        all_ch=Members.objects.all().filter(channel=room_name).values_list('member', flat=True).order_by('id')
        return render(request, 'room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
         'all_ch':all_ch,
        })
    else:
        return HttpResponseRedirect(reverse('login'))

def Channel_create(request,roomName):
    us=Channels()
    us.creator=request.session.get('name')
    us.channel=roomName
    us2=Members()
    us2.member=request.session.get('name')
    us2.channel=roomName
    us2.save()
    err=None
    try:
        us.save()
    except:
        err="room already exists"
        return HttpResponseRedirect(reverse('dashboard',args=(request.session.get('name'),)))
    return HttpResponseRedirect(reverse('room',args=(roomName,)))

def Join_room(request,room_name):
    us=Members()
    user=request.session.get('name')
    err=None
    if Members.objects.filter(member=user,channel=room_name).exists():
       err="already a member"
    else:
        us.member=user
        us.channel=room_name
        print("here")
        us.save()
    return render(request, 'room.html', {
    'room_name_json': mark_safe(json.dumps(room_name)),
    'err':err,
    })

    '''def Create_channel(request,room_name):
    if request.session.get('name'):
        us=Channels()
        us.user=request.session.get('name')
        channel=room_name
        us.save()
        return HttpResponseRedirect(reverse('room',args=(room_name,)))'''
