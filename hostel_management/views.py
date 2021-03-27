from django.shortcuts import render
from .models import Student, Warden, CustomUser, GH1, GH2, GH3, GH4, BH1, BH2, BH3, BH4, WaitingTable, Complaint, Building
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout
from hostel_management.EmailBackEnd import EmailBackEnd
from django.contrib import messages


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

def wardenDashboard(request):
    return render(request, 'wardenDashboard.html', {})


def room_register134(request):
    return render(request, '1_3_4_room_register.html')


def room_register2(request):
    return render(request, '2_room_register.html')


def waiting_table_form(request):
    return render(request, 'waiting_form.html')


def complainForm(request):
    return render(request, 'complainForm.html')


def dosignout(request):
    logout(request)
    return render(request, 'home.html')


def complainFormSubmission(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        roll_no = request.POST.get('roll_no')
        complainText = request.POST.get('complainText')
        student = Student.objects.get(roll_no=roll_no)
        complain = Complaint(roll_no=student, complaintText=complainText)
        complain.save()
        return render(request, 'studentDashboard.html', {})


def register_form_submission(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        if request.method == 'POST':

            roll_no = request.POST.get('username')
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            username = request.POST.get("username")
            branch = request.POST.get('branch')
            year = request.POST.get('year')
            email = request.POST.get('email')
            contact_number = request.POST.get('contact')
            password = request.POST.get('password')
            gender = request.POST.get('gender')

            if CustomUser.objects.filter(email=email).exists():
                print('user already exists')
                messages.info(request,"Email already exists")
                return render(request, 'Register1.html', {})

            if CustomUser.objects.filter(username=username).exists():
                print('username already taken')
                messages.info(request,"Username already exists")
                return render(request, 'Register1.html', {})

            if Student.objects.filter(roll_no=roll_no).exists():
                print('Student already registered')
                messages.info(request,"Roll no. already registered")
                return render(request, 'Register.html', {})

            user = CustomUser.objects.create_user(
                username=username, password=password, email=email, last_name=last_name, first_name=first_name, user_type=3)
            user.student.roll_no = roll_no
            user.student.branch = branch
            user.student.year = year
            user.student.gender = gender
            user.student.contact_number = contact_number

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
            block_name = request.POST.get('block')

            if CustomUser.objects.filter(email=email).exists():
                print('user already exists')
                messages.info(request,"Email already exists")
                return render(request, 'RegisterWarden.html', {})

            if CustomUser.objects.filter(username=username).exists():
                print('username already taken')
                messages.info(request,"Username already exists")
                return render(request, 'RegisterWarden.html', {})

            user = CustomUser.objects.create_user(
                username=username, password=password, email=email, last_name=last_name, first_name=first_name, user_type=2)
            user.warden.gender = gender
            user.warden.department = department
            user.warden.contact = contact_number
            block=Building.objects.get(block_name=block_name)
            user.warden.block_name=block
            user.save()
            return render(request, 'signin.html', {})


def dosigninWarden(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get(
            "email"), password=request.POST.get("password"))
        if user != None:
            login(request, user, backend='hostel_management.EmailBackEnd.EmailBackEnd')
            warden = CustomUser.objects.get(id=request.user.id)
            block=Warden.objects.get(admin_id=warden.id).block_name
            if user.user_type == "2":
                return render(request, 'wardenDashboard.html', context={'warden':warden, 'block':block})
            else:
                messages.info(request,"Invalid Email or Password")
                return render(request, 'signin.html', {})
        else:
            messages.info(request,"Invalid Email or Password")
            return render(request, 'signin.html', {})


def dosigninStudent(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get(
            "email"), password=request.POST.get("password"))
        if user != None:
            login(request, user, backend='hostel_management.EmailBackEnd.EmailBackEnd')
            admin_id = user.id
            student = Student.objects.get(admin_id=admin_id)
            if user.user_type == "3":
                return render(request, 'studentDashboard.html', {"student": student, "user":user})
            else:
                messages.info(request,"Invalid Email or Password")
                return render(request, 'signin.html', {})
        else:
            messages.info(request,"Invalid Email or Password")
            return render(request, 'signin.html', {})


def room_register_1_3_4(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        roll_no = request.POST.get('roll_no')
        name = request.POST.get('name')
        year = request.POST.get('year')
        gender = request.POST.get('gender')
        contact_number = request.POST.get('contact')

        if Student.objects.filter(roll_no=roll_no).exists() == False:
            print('student does not exist')
            return render(request, 'studentDashboard.html', {})

        print(type(year))

        if int(year) == 1:

            if gender == "Female":

                if GH1.objects.filter(roll_1=roll_no).exists() or GH1.objects.filter(roll_2=roll_no).exists() or GH1.objects.filter(roll_3=roll_no).exists():
                    print('Room already allocated')
                    return render(request, 'studentDashboard.html', {})

                latest_room = GH1.objects.order_by('room_no').last()
                print(latest_room)
                if latest_room == None:
                    new_room = GH1(room_no=101, roll_1=roll_no)
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
                    room_no = 100*(quotient+1) + mod + 1
                    room = GH1(room_no=room_no, roll_1=roll_no)
                    room.save()
            else:
                if BH1.objects.filter(roll_1=roll_no).exists() or BH1.objects.filter(roll_2=roll_no).exists() or BH1.objects.filter(roll_3=roll_no).exists():
                    print('Room already allocated')
                    return render(request, 'studentDashboard.html', {})

                latest_room = BH1.objects.order_by('room_no').last()
                print(latest_room)
                if latest_room == None:
                    new_room = BH1(room_no=101, roll_1=roll_no)
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
                    room_no = 100*(quotient+1) + mod + 1
                    room = BH1(room_no=room_no, roll_1=roll_no)
                    room.save()

        elif int(year) == 3 or int(year) == 4:
            if gender == "Female":
                if int(year) == 3 and GH3.objects.filter(roll_1=roll_no).exists():
                    print("Room already allocated")
                    return render(request, 'studentDashboard.html', {})
                elif int(year) == 4 and GH4.objects.filter(roll_1=roll_no).exists():
                    print("Room already allocated")
                    return render(request, 'studentDashboard.html', {})
            else:
                if int(year) == 3 and BH3.objects.filter(roll_1=roll_no).exists():
                    print("Room already allocated")
                    return render(request, 'studentDashboard.html', {})
                elif int(year) == 4 and BH4.objects.filter(roll_1=roll_no).exists():
                    print("Room already allocated")
                    return render(request, 'studentDashboard.html', {})

            if gender == "Female":
                if int(year) == 3:
                    latest_count = GH3.objects.count()
                else:
                    latest_count = GH4.objects.count()
                mod = latest_count % 75
                quotient = int(latest_count / 75)
                room_no = 100*(quotient+1) + mod + 1
                if int(year) == 3:
                    room = GH3(room_no=room_no, roll_1=roll_no)
                else:
                    room = GH4(room_no=room_no, roll_1=roll_no)
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
                    room = BH3(room_no=room_no, roll_1=roll_no)
                else:
                    room = BH4(room_no=room_no, roll_1=roll_no)
                room.save()

        print('room saved')
        return render(request, 'studentDashboard.html', {})


def room_register_2(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        roll_1 = request.POST.get('roll_1')
        roll_2 = request.POST.get('roll_2')
        name_1 = request.POST.get('name_1')
        name_2 = request.POST.get('name_2')
        year = request.POST.get('year')
        gender = request.POST.get('gender')

        if gender == "Female":
            if GH2.objects.filter(roll_1=roll_1).exists() or GH2.objects.filter(roll_2=roll_1).exists():
                print("Roll no 1 already allocated room")
                return render(request, 'studentDashboard.html', {})
            if GH2.objects.filter(roll_1=roll_2).exists() or GH2.objects.filter(roll_2=roll_2).exists():
                print("Roll no 2 already allocated room")
                return render(request, 'studentDashboard.html', {})

            latest_count = GH2.objects.count()
            mod = latest_count % 50
            quotient = int(latest_count / 50)
            room_no = 100*(quotient+1) + mod + 1
            room = GH2(room_no=room_no, roll_1=roll_1, roll_2=roll_2)
            room.save()
        else:
            if BH2.objects.filter(roll_1=roll_1).exists() or BH2.objects.filter(roll_2=roll_1).exists():
                print("Roll no 1 already allocated room")
                return render(request, 'studentDashboard.html', {})
            if BH2.objects.filter(roll_1=roll_2).exists() or BH2.objects.filter(roll_2=roll_2).exists():
                print("Roll no 2 already allocated room")
                return render(request, 'studentDashboard.html', {})

            latest_count = BH2.objects.count()
            mod = latest_count % 50
            quotient = int(latest_count / 50)
            room_no = 100*(quotient+1) + mod + 1
            room = BH2(room_no=room_no, roll_1=roll_1, roll_2=roll_2)
            room.save()

        print('room saved')
        return render(request, 'studentDashboard.html', {})


def waiting_table(request):
    roll_1 = request.POST.get('roll_no')
    gender = request.POST.get('gender')

    if gender == "Female":
        if GH2.objects.filter(roll_1=roll_1).exists() or GH2.objects.filter(roll_2=roll_1).exists():
            print("Roll no 1 already allocated room")
            return render(request, 'studentDashboard.html', {})
    else:
        if BH2.objects.filter(roll_1=roll_1).exists() or BH2.objects.filter(roll_2=roll_1).exists():
            print("Roll no 1 already allocated room")
            return render(request, 'studentDashboard.html', {})

    if WaitingTable.objects.filter(roll_no=roll_1).exists():
        print('Roll no already in waiting table')
        return render(request, 'studentDashboard.html', {})

    count = WaitingTable.objects.filter(gender=gender).count()
    if count == 0:
        add_student = WaitingTable(roll_no=roll_1, gender=gender)
        add_student.save()
    elif gender == "Female":
        roll_2 = WaitingTable.objects.filter(gender=gender).first().roll_no
        print(roll_2)
        latest_count = GH2.objects.count()
        mod = latest_count % 50
        quotient = int(latest_count / 50)
        room_no = 100*(quotient+1) + mod + 1
        room = GH2(room_no=room_no, roll_1=roll_1, roll_2=roll_2)
        room.save()
        WaitingTable.objects.filter(roll_no=roll_2).delete()
    else:
        roll_2 = WaitingTable.objects.filter(gender=gender).first().roll_no
        latest_count = BH2.objects.count()
        mod = latest_count % 50
        quotient = int(latest_count / 50)
        room_no = 100*(quotient+1) + mod + 1
        room = BH2(room_no=room_no, roll_1=roll_1, roll_2=roll_2)
        room.save()

    return render(request, 'studentDashboard.html', {})


def contactUs(request):
    objs = CustomUser.objects.filter(user_type="2")
    objs1 = Warden.objects.all()
    return render(request, 'contactUs.html', {'objs': objs, 'objs1': objs1})



def viewComplain(request):
    complain = Complaint.objects.all()
    return render(request, 'viewComplain.html', {'complain': complain, 'user':CustomUser})
