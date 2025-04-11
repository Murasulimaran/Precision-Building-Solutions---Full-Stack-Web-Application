from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User,auth
from django.contrib import messages
import re


# Create your views here.


def index_view(request):
    return render(request,'index.html')


def quote_view(request):
    return render(request,'freequote.html')

def payment(request):
    return render(request,'payment.html')


def register_view(request):
    if request.method == 'POST':
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d@#$%^&+=]{8,}$'

        if not re.match(password_regex, password):
            messages.error(request,'Password At least 8 characters need!')
            return redirect('/register/')

        if password != confirm_password:
            messages.error(request,'Password does not match!')
            return redirect('/register/')

        if User.objects.filter(username=username).exists():
            messages.error(request,'This username is already used!')
            return redirect('/register/')

        else:
            user = User.objects.create_user(first_name=firstname, last_name=lastname,
                                           username=username, email=email, password=password)
            user.set_password(password)
            user.save()
            messages.success(request, 'successfully completed your regeneration')
            return redirect('/login/')

    return render(request,'registration.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/payment/')
        else:
            messages.error(request,'Username or Password are incorrect!')
            return redirect('/login/')
    return render(request,'login.html')