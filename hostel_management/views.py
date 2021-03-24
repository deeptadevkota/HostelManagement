from django.shortcuts import render
from .models import Student, Warden, CustomUser
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login
# Create your views here.

from hostel_management.EmailBackEnd import EmailBackEnd


def home(request):
    return render(request, 'home.html', {})


def register(request):
    return render(request, 'Register1.html', {})

def registerWarden(request):
    return render(request, 'RegisterWarden.html', {})

def signin(request):
    return render(request, 'signin.html', {})


def signinwarden(request):
    return render(request, 'signinWarden.html', {})


def dashboard(request):
    return render(request, 'studentDashboard.html', {})


def register_form_submission(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        if request.method == 'POST':
            roll_no = request.POST.get('roll_no')
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            username = request.POST.get("username")
            branch = request.POST.get('branch')
            year = request.POST.get('year')
            email = request.POST.get('email')
            contact_number = request.POST.get('contact')
            password = request.POST.get('password')
            user = CustomUser.objects.create_user(
            username=username, password=password, email=email, last_name=last_name, first_name=first_name, user_type=3)        
            user.student.roll_no=roll_no
            user.student.branch=branch
            user.student.year=year
            user.student.contact_number=contact_number
            user.save()
            return render(request, 'signin.html', {})

def registerWarden_form_submission(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        if request.method == 'POST':
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            username = request.POST.get("username")
            department = request.POST.get('branch')
            email = request.POST.get('email')
            contact_number = request.POST.get('contact')
            password = request.POST.get('password')
            gender = request.POST.get('gender')
            user = CustomUser.objects.create_user(
            username=username, password=password, email=email, last_name=last_name, first_name=first_name, user_type=2)        
            user.warden.gender=gender
            user.warden.department=department
            user.warden.contact=contact_number
            user.save()
            return render(request, 'signin.html', {})

def dosigninWarden(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get("email"), password=request.POST.get("password"))
        if user != None:
            login(request, user, backend='hostel_management.EmailBackEnd.EmailBackEnd')
            if user.user_type == "2":
                return render(request, 'home.html', {})
            else:
                return render(request, 'signin.html', {})
        else:
            return render(request, 'signin.html', {})

def dosigninStudent(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get("email"), password=request.POST.get("password"))
        if user != None:
            login(request, user, backend='hostel_management.EmailBackEnd.EmailBackEnd')
            if user.user_type == "3":
                return render(request, 'studentDashboard.html', {})
            else:
                return render(request, 'signin.html', {})
        else:
            return render(request, 'signin.html', {})

def contactUs(request):
    objs=CustomUser.objects.filter(user_type="2")
    objs1=Warden.objects.all()
    return render(request,'contactUs.html',{'objs':objs, 'objs1': objs1})