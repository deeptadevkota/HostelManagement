from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html',{})

def register(request):
    return render(request, 'Register1.html',{})

def signin(request):
    return render(request, 'signin.html',{})

def signinwarden(request):
    return render(request, 'signinWarden.html',{})

def dashboard(request):
    return render(request, 'studentDashboard.html',{})