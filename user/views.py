from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from .forms import *

# Create your views here.

def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password')
            username = CustomUser.objects.get(email=email).username
            user = authenticate(request, username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                return render(request,'login.html',{'form':form})
    form = LoginForm()
    return render(request,'login.html',{'form':form})


def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request,'register.html',{'form':form})


    form = RegisterForm()
    return render(request,'register.html',{'form':form})
def user_logout(request):
    logout(request)
    return redirect('index')