from django.shortcuts import render
from .models import Student
# Create your views here.


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
        password=request.POST.get('password')
        student = Student(name=name, roll_no=roll_no, branch=branch,
                          year=year, email=email, contact_number=contact_number, password=password)
        student.save()
    return render(request, 'signin.html', {})
