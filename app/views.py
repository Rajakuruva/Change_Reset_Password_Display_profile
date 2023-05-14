from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from app.forms import *
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.
def Home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request,'Home.html',d)
    return render(request,'Home.html')

def Registartion(request):
    UO=Userform()
    PO=ProfileForm()
    d={"UO":UO,"PO":PO}
    if request.method=='POST' and request.FILES:
        USO=Userform(request.POST)
        PSO=ProfileForm(request.POST,request.FILES)
        if USO.is_valid() and PSO.is_valid():
            NSUO=USO.save(commit=False)
            NSUO.set_password(USO.cleaned_data['password'])
            NSUO.save()
            NSPO=PSO.save(commit=False)
            NSPO.username=NSUO
            NSPO.save()
            send_mail('Register',
                      'Register is done',
                      'kuruvarajasekhar2019@gmail.com',
                      [NSUO.email],
                      fail_silently=False
                      )
            return HttpResponse("Registeration is completed!!!")
        else:
            return HttpResponse("Invalid Data")
    return render(request,'Registartion.html',d)

def User_login(requset):
    if requset.method=='POST':
        username=requset.POST['username']
        password=requset.POST['password']
        AUO=authenticate(username=username,password=password)
        if AUO and AUO.is_active:
            login(requset,AUO)
            requset.session['username']=username
            return HttpResponseRedirect(reverse('Home'))
        else:
            return HttpResponse("Inavalid Username or password!!!")
    return render(requset,'User_login.html')

@login_required
def Log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse("Home"))

@login_required
def Display_Profile(request):
    username=request.session.get('username')
    UO=User.objects.get(username=username)
    PO=Profile.objects.get(username=UO)
    d={"UO":UO,"PO":PO}
    return render(request,"Display_Profile.html",d)

@login_required
def Change_password(request):
    if request.method=='POST':
        pw=request.POST['pw']
        username=request.session.get('username')
        UO=User.objects.get(username=username)
        UO.set_password(pw)
        UO.save()
        
        return HttpResponse("Password change successfully!!!")    
    return render(request,'Change_password.html')

def Forgot_Password(request):
    if request.method=='POST':
        un=request.POST['un']
        pw=request.POST['pw']
        LUO=User.objects.filter(username=un)
        if LUO:
            UO=LUO[0]
            UO.set_password(pw)
            UO.save()
            return HttpResponse("Password reset is done")
        else:
            return HttpResponse("Username is not avaliable")

    return render(request,'Forgot_Password.html')