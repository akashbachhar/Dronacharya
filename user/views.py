from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def handle_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            return redirect('handle_login')

    return render(request, 'user/signup.html')


def handle_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('handle_login')

    return render(request, 'user/login.html')


def handle_logout(request):
    logout(request)
    return redirect('dashboard')
