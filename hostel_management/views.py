from django.shortcuts import render
from .models import Student, Warden, CustomUser, GH1, GH2, GH3, GH4, BH1, BH2, BH3, BH4
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
            username=username, password=password, email=email, last_name=last_name, first_name=first_name, user_type=2)        
            user.student.roll_no=roll_no
            user.student.branch=branch
            user.student.year=year
            user.student.contact_number=contact_number
            user.save()

            if gender == "Female":
                latest_room = GH1.objects.order_by('room_no').last()
                print(latest_room)

                if latest_room == None:
                    new_room = GH1(room_no = 101, roll_1 = roll_no)
                    new_room.save()
                elif latest_room.roll_2 == None:
                    latest_room.roll_2 = roll_no
                    latest_room.save()
                elif latest_room.roll_3 == None:
                    latest_room.roll_3 = roll_no
                    latest_room.save()
                else:
                    latest_count = GH1.objects.count()
                    mod = latest_count % 25
                    quotient = int(latest_count / 25)
                    print()
                    room_no = 100*(quotient+1) + mod +1
                    room = GH1(room_no = room_no, roll_1 = roll_no)
                    room.save()
            else:
                latest_room = BH1.objects.order_by('room_no').last()

                print(latest_room)

                if latest_room == None:
                    new_room = BH1(room_no = 101, roll_1 = roll_no)
                    new_room.save()
                elif latest_room.roll_2 == None:
                    latest_room.roll_2 = roll_no
                    latest_room.save()
                elif latest_room.roll_3 == None:
                    latest_room.roll_3 = roll_no
                    latest_room.save()
                else:
                    latest_count = BH1.objects.count()
                    mod = latest_count % 25
                    quotient = int(latest_count / 25)
                    print()
                    room_no = 100*(quotient+1) + mod +1
                    room = BH1(room_no = room_no, roll_1 = roll_no)
                    room.save()
            print("Student created")
            return render(request, 'signin.html', {})

def dosigninWarden(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get("email"), password=request.POST.get("password"))
        if user != None:
            login(request, user)
            if user.user_type == "1":
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
            login(request, user)
            if user.user_type == "2":
                return render(request, 'studentDashboard.html', {})
            else:
                return render(request, 'signin.html', {})
        else:
            return render(request, 'signin.html', {})


def room_register(request):
    return render(request, '3Y4Y_room_register.html')


def room_register_3_4(request):
    if request.method == "POST":
        roll_no = request.POST.get('roll_no')
        name = request.POST.get('name')
        year = request.POST.get('year')
        gender = request.POST.get('gender')
        contact_number = request.POST.get('contact')
        
        print(type(year))

        if gender == "Female":
            if int(year) == 3 and GH3.objects.filter(roll_1 = roll_no).exists():
                print("Room already allocated")
                return render(request, 'studentDashboard.html', {})
            elif int(year) == 4 and GH4.objects.filter(roll_1 = roll_no).exists():
                print("Room already allocated")
                return render(request, 'studentDashboard.html', {})
        else:
            if int(year) == 3 and BH3.objects.filter(roll_1 = roll_no).exists():
                print("Room already allocated")
                return render(request, 'studentDashboard.html', {})
            elif int(year) == 4 and BH4.objects.filter(roll_1 = roll_no).exists():
                print("Room already allocated")
                return render(request, 'studentDashboard.html', {})


        if gender == "Female":
            if int(year) == 3:
                latest_count = GH3.objects.count()
            else:
                latest_count = GH4.objects.count()
            print(latest_count)
            mod = latest_count % 75
            quotient = int(latest_count / 75)
            print(mod, quotient)
            room_no = 100*(quotient+1) + mod +1
            if int(year) == 3:
                room = GH3(room_no = room_no, roll_1 = roll_no)
            else:
                room = GH4(room_no = room_no, roll_1 = roll_no)
            room.save()

        else:
            if int(year) == 3:
                latest_count = BH3.objects.count()
            else:
                latest_count = BH4.objects.count()
            mod = latest_count % 75
            quotient = int(latest_count / 75)
            room_no = 100*(quotient+1) + mod + 1
            if student.year == 3:
                room = BH3(room_no = room_no, roll_1 = roll_no)
            else:
                room = BH4(room_no = room_no, roll_1 = roll_no)
            room.save()
            
        print('room saved')

        return render(request, 'studentDashboard.html', {})