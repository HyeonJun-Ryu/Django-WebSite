from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def accounts(request):
    return render(request, 'accounts.html')

def terms(request):
    return render(request, 'terms.html')    


def signup(request):
    
    if request.method == "POST":
        if request.POST.get("password1") == request.POST.get("password2"):

            user = User.objects.create_user(
                username=request.POST.get("username"), password=request.POST.get("password1"))
            auth.login(request, user)
            return redirect('/index')
        else:   
            return render(request, 'signup.html')

    return render(request, 'signup.html')

def login(request):
    response_data = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/index')
        else:
            return render(request, 'login.html')
            
    else:
        return render(request, 'login.html')
    

def logout(request):
    auth.logout(request)
    return redirect('index')

