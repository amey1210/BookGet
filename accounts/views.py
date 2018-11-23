from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from .models import MyUser
from .forms import RegisterForm
from django.http import *
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    return render(request,'accounts/home.html')

def login_user(request):
    logout(request)
    context = RequestContext(request)
    email = password = ''
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email,password=password)
        if user is not None:
            print (user.get_full_name())
            login(request,user)
            return redirect('shop:product_list')
        else:
            print("hi")
            messages.error(request,"Invalid Username or Wrong password")
            return render(request,'accounts/login.html')
    else:
        return render(request,'accounts/login.html')

#@login_required(login_url='/login/')

def logout_user(request):
    logout(request)
    return redirect('shop:product_list')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if form.clean_email():
                if form.clean_password2():
                    user = form.save()
                    raw_password = form.cleaned_data.get('password1')
                    user = authenticate(email=user.email, password=raw_password)
                    login(request, user)
                    return redirect('shop:product_list')
                else:
                    messages.error(request,"Passwords don't match")
                    redirect ('/account/register/')
            else:
                messages.error(request,"Email is taken")
                redirect('/account/register/')
        else:
            messages.error(request, "There is error in form")
            redirect('/account/register/')
    else:
        form = RegisterForm()
        return render(request,'accounts/register.html',{'form': form})
