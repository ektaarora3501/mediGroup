from django.shortcuts import render,redirect
from group.models import Register
from django.urls import reverse,reverse_lazy
from group.forms import SignupForm,LoginForm
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
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


def logout(request,user):
    try:
        del request.session['name']
        print("user deleted")
        print(request.session['name'])
    except :
          pass
    return HttpResponseRedirect(reverse('login'))
