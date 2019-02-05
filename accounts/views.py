from django.shortcuts import render

def accounts(request):
    return render(request, 'accounts.html')

def logout(request):
    return render(request, 'logout.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')
