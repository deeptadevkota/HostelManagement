from django.shortcuts import render
from .models import Student
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login
# Create your views here.

from hostel_management.EmailBackEnd import EmailBackEnd


def home(request):
    return render(request, 'home.html', {})


def register(request):
    return render(request, 'Register1.html', {})


def signin(request):
    return render(request, 'signin.html', {})


def signinwarden(request):
    return render(request, 'signinWarden.html', {})


def dashboard(request):
    return render(request, 'studentDashboard.html', {})


def register_form_submission(request):
    if request.method == 'POST':
        roll_no = request.POST.get('roll_no')
        name = request.POST.get('name')
        branch = request.POST.get('branch')
        year = request.POST.get('year')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact')
        password = request.POST.get('password')
        student = Student(name=name, roll_no=roll_no, branch=branch,
                          year=year, email=email, contact_number=contact_number, password=password)
        student.save()
    return render(request, 'signin.html', {})


def dosigninWarden(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get(
            "email"), password=request.POST.get("password"))
        if user != None:
            login(request, user)
            if user.user_type == "1":
                return render(request, 'home.html', {})
            elif user.user_type == "2":
                return render(request, 'home.html', {})
            else:
                return render(request, 'home.html', {})
        else:
            return render(request, 'signin.html', {})
