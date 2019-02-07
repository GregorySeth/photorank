from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def success(request):
    return render(request, 'accounts/success.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return render(request, 'accounts/logout.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if not user == None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error':'Nieprawidłowy użytkownik, lub hasło.'})
    else:
        return render(request, 'accounts/login.html')

def signup(request):
    if request.method == 'POST':
        #User wants to sign up
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Taki użytkownik już istnieje.'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('success')
        else:
            return render(request, 'accounts/signup.html', {'error':'Podane hasła różnią się od siebie.'})
    else:
        #User wants to enter info
        return render(request, 'accounts/signup.html')
