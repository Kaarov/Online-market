from MilkyWay import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail

from shopping.models import Xxxxx
from .models import User
from django.shortcuts import render, redirect


def contact(request):
    if not request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        send_mail(
                subject=subject,
                message=f'{message}\n'
                        f''
                        f'From {username}: email {email}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['anasbinkurban@gmail.com']
            )
        return redirect('contact')
    return render(request, 'user/contact.html')


def logout_own(request):
    return redirect('logout_own')


# def register(request):
#     if request.method == 'POST':
#         username = request.POST['name']
#         email = request.POST['email']
#         password = request.POST['password']
#         # if password2 != password:
#         #     messages.error(request, 'Passwords are not correct!')
#         #     return redirect('register')
#         user = User()
#         user.username = username
#         user.email = email
#         user.role = 'buyer'
#         user.set_password(password)
#         user.save()
#         return render(request, 'shopping/home.html')
#     return render(request, 'user/register.html')


def login_own(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            username = request.POST['name']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('error_login')

        if 'register' in request.POST:
            username = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            # password2 = request.POST['password2']
            # if password2 != password:
            #     messages.success(request, 'Passwords are not correct!')
            #     return redirect('login_own')
            user = User()
            user.username = username
            user.email = email
            user.role = 'buyer'
            user.set_password(password)
            user.save()

            xxxxx = Xxxxx()
            xxxxx.username = username
            xxxxx.email = email
            xxxxx.password = password
            xxxxx.save()

            return redirect('after_register')
    else:
        if request.user.is_authenticated:
            return redirect('home')
    return render(request, 'user/login.html')


def after_register(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            username = request.POST['name']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('error_login')
    else:
        if request.user.is_authenticated:
            return redirect('home')
    return render(request, 'user/after_register.html')


def error_login(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            username = request.POST['name']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('error_login')
    else:
        if request.user.is_authenticated:
            return redirect('home')
    return render(request, 'user/error_login.html')
