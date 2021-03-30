from django.shortcuts import render
from .models import Student, Warden, CustomUser, GH1, GH2, GH3, GH4, BH1, BH2, BH3, BH4, WaitingTable, Complaint, Building, room_Allocation
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout
from hostel_management.EmailBackEnd import EmailBackEnd
from django.contrib import messages


def home(request):
    return render(request, 'home.html', {})

def register(request):
    return render(request, 'Register1.html', {})

def registerWarden(request):
    blocks = Building.objects.all()
    print(blocks)
    return render(request, 'RegisterWarden.html', {"blocks":blocks})

def signin(request):
    return render(request, 'signin.html', {})

def signinwarden(request):
    return render(request, 'signinWarden.html', {})

def dashboard(request):
    admin_id = request.user.id
    student = Student.objects.get(admin_id=admin_id)
    roll_no = student.roll_no
    year = student.year
    gender = student.gender
    r_block = check_room(roll_no,year,gender)
    return render(request, 'studentDashboard.html', {"student":student, "r_block" : r_block})

def wardenDashboard(request):
    return render(request, 'wardenDashboard.html', {})

def room_register134(request):
    admin_id = request.user.id
    student = Student.objects.get(admin_id=admin_id)
    roll_no = student.roll_no
    year = student.year
    gender = student.gender
    r_block = check_room(roll_no,year,gender)
    return render(request, '1_3_4_room_register.html',{"student":student, 'r_block':block})

def room_register2(request):
    admin_id = request.user.id
    student = Student.objects.get(admin_id=admin_id)
    roll_no = student.roll_no
    year = student.year
    gender = student.gender
    r_block = check_room(roll_no,year,gender)
    return render(request, '2_room_register.html',{"student":student, "r_block" : r_block})

def waiting_table_form(request):
    admin_id = request.user.id
    student = Student.objects.get(admin_id=admin_id)
    roll_no = student.roll_no
    year = student.year
    gender = student.gender
    r_block = check_room(roll_no,year,gender)
    return render(request, 'waiting_form.html',{"student":student, "r_block" : r_block})

def complainForm(request):
    admin_id = request.user.id
    student = Student.objects.get(admin_id=admin_id)
    roll_no = student.roll_no
    year = student.year
    gender = student.gender
    r_block = check_room(roll_no,year,gender)
    return render(request, 'complainForm.html',{"student":student, "r_block" : r_block})

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
            print(block)
            user.warden.block_name=block
            user.save()
            print('saved')
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
                roll_no = student.roll_no
                year = student.year
                gender = student.gender
                r_block = check_room(roll_no,year,gender)
                is_set=room_Allocation.objects.all()[0].is_room_allocation_set
                print("**********************")
                return render(request, 'studentDashboard.html', {"student": student, "user":user, "r_block" : r_block, "is_set":is_set})
            else:
                messages.info(request,"Invalid Email or Password")
                return render(request, 'signin.html', {})
        else:
            messages.info(request,"Invalid Email or Password")
            return render(request, 'signin.html', {})

def check_room(roll_no, year, gender):
    room = 0
    block = None
    if int(year) == 1:
        if gender == "Female":
            if GH1.objects.filter(roll_1 = roll_no).exists():
                room = GH1.objects.get(roll_1 = roll_no).room_no
                block = "GH1"
            elif GH1.objects.filter(roll_2 = roll_no).exists():
                room = GH1.objects.get(roll_2 = roll_no).room_no
                block = "GH1"
            elif GH1.objects.filter(roll_3 = roll_no).exists():
                room = GH1.objects.get(roll_3 = roll_no).room_no
                block = "GH1"
        else:
            if BH1.objects.filter(roll_1 = roll_no).exists():
                room = BH1.objects.get(roll_1 = roll_no).room_no
                block = "BH1"
            if BH1.objects.filter(roll_2 = roll_no).exists():
                room = BH1.objects.get(roll_2 = roll_no).room_no
                block = "BH1"
            if BH1.objects.filter(roll_3 = roll_no).exists():
                room = BH1.objects.get(roll_3 = roll_no).room_no
                block = "BH1"
    elif int(year) == 2:
        if gender == "Female":
            if GH2.objects.filter(roll_1 = roll_no).exists():
                room = GH2.objects.get(roll_1 = roll_no).room_no
                block = "GH2"
            elif GH2.objects.filter(roll_2 = roll_no).exists():
                room = GH2.objects.get(roll_2 = roll_no).room_no
                block = "GH2"
        else:
            if BH2.objects.filter(roll_1 = roll_no).exists():
                room = BH2.objects.get(roll_1 = roll_no).room_no
                block = "BH2"
            elif BH2.objects.filter(roll_2 = roll_no).exists():
                room = BH2.objects.get(roll_2 = roll_no).room_no
                block = "BH2"
    elif int(year) == 3:
        if gender == "Female":
            if GH3.objects.filter(roll_1 = roll_no).exists():
                room = GH3.objects.get(roll_1 = roll_no).room_no
                block = "GH3"
        else:
            if BH3.objects.filter(roll_1 = roll_no).exists():
                room = BH3.objects.get(roll_1 = roll_no).room_no
                block = "BH3"
    elif int(year) == 4:
        if gender == "Female":
            if GH4.objects.filter(roll_1 = roll_no).exists():
                room = GH4.objects.get(roll_1 = roll_no).room_no
                block = "GH4"
        else:
            if BH4.objects.filter(roll_1 = roll_no).exists():
                room = BH4.objects.get(roll_1 = roll_no).room_no
                block = "BH4"
    r_block = {"room" : room , "block" : block}
    return r_block
    

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
            return render(request, 'signin.html', {})

        print(type(year))

        if int(year) == 1:

            if gender == "Female":

                if GH1.objects.filter(roll_1=roll_no).exists() or GH1.objects.filter(roll_2=roll_no).exists() or GH1.objects.filter(roll_3=roll_no).exists():
                    print('Room already allocated')
                    r_block = check_room(roll_no,year,gender)
                    return render(request, 'studentDashboard.html', {"r_block":r_block})

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
                    r_block = check_room(roll_no,year,gender)
                    return render(request, 'studentDashboard.html', {"r_block":r_block})

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
                    r_block = check_room(roll_no,year,gender)
                    return render(request, 'studentDashboard.html', {"r_block":r_block})
                elif int(year) == 4 and GH4.objects.filter(roll_1=roll_no).exists():
                    print("Room already allocated")
                    r_block = check_room(roll_no,year,gender)
                    return render(request, 'studentDashboard.html', {"r_block":r_block})
            else:
                if int(year) == 3 and BH3.objects.filter(roll_1=roll_no).exists():
                    print("Room already allocated")
                    r_block = check_room(roll_no,year,gender)
                    return render(request, 'studentDashboard.html', {"r_block":r_block})
                elif int(year) == 4 and BH4.objects.filter(roll_1=roll_no).exists():
                    print("Room already allocated")
                    r_block = check_room(roll_no,year,gender)
                    return render(request, 'studentDashboard.html', {"r_block":r_block})

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
        r_block = check_room(roll_no,year,gender)
        return render(request, 'studentDashboard.html', {"r_block":r_block})


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

        # admin1 = Student.objects.get(roll_no = roll_1).admin_id
        # admin2 = Student.objects.get(roll_no = roll_2).admin_id
        admin_id = request.user.id
        sign_student = Student.objects.get(admin_id = admin_id)
        roll_no = sign_student.roll_no
        gender = sign_student.gender

        if gender == "Female":
            if GH2.objects.filter(roll_1=roll_1).exists() or GH2.objects.filter(roll_2=roll_1).exists():
                print("Roll no 1 already allocated room")
                messages.info(request,"Student 1 already allocated room")
                r_block = check_room(roll_no,year,gender)
                return render(request, 'studentDashboard.html', {"r_block":r_block})
            if GH2.objects.filter(roll_1=roll_2).exists() or GH2.objects.filter(roll_2=roll_2).exists():
                print("Roll no 2 already allocated room")
                messages.info(request,"Student 2 already allocated room")
                r_block = check_room(roll_no,year,gender)
                return render(request, 'studentDashboard.html', {"r_block":r_block})

            latest_count = GH2.objects.count()
            mod = latest_count % 50
            quotient = int(latest_count / 50)
            room_no = 100*(quotient+1) + mod + 1
            room = GH2(room_no=room_no, roll_1=roll_1, roll_2=roll_2)

            if WaitingTable.objects.filter(roll_no=roll_1).exists():
                WaitingTable.objects.filter(roll_no=roll_1).delete()
            if WaitingTable.objects.filter(roll_no=roll_2).exists():
                WaitingTable.objects.filter(roll_no=roll_2).delete()
        
            room.save()
        else:
            if BH2.objects.filter(roll_1=roll_1).exists() or BH2.objects.filter(roll_2=roll_1).exists():
                print("Roll no 1 already allocated room")
                messages.info(request,"Student 1 already allocated room")
                r_block = check_room(roll_no,year,gender)
                return render(request, 'studentDashboard.html', {"r_block":r_block})
            if BH2.objects.filter(roll_1=roll_2).exists() or BH2.objects.filter(roll_2=roll_2).exists():
                print("Roll no 2 already allocated room")
                messages.info(request,"Student 2 already allocated room")
                r_block = check_room(roll_no,year,gender)
                return render(request, 'studentDashboard.html', {"r_block":r_block})

            latest_count = BH2.objects.count()
            mod = latest_count % 50
            quotient = int(latest_count / 50)
            room_no = 100*(quotient+1) + mod + 1
            room = BH2(room_no=room_no, roll_1=roll_1, roll_2=roll_2)

            if WaitingTable.objects.filter(roll_no=roll_1).exists():
                WaitingTable.objects.filter(roll_no=roll_1).delete()
            if WaitingTable.objects.filter(roll_no=roll_2).exists():
                WaitingTable.objects.filter(roll_no=roll_2).delete()

            room.save()

        print('room saved')
        r_block = check_room(roll_no,year,gender)
        return render(request, 'studentDashboard.html', {"r_block":r_block})


def waiting_table(request):
    roll_1 = request.POST.get('roll_no')
    gender = request.POST.get('gender')

    if gender == "Female":
        if GH2.objects.filter(roll_1=roll_1).exists() or GH2.objects.filter(roll_2=roll_1).exists():
            print("Roll no 1 already allocated room")
            messages.info(request,"Room already allocated")
            r_block = check_room(roll_no,year,gender)
            return render(request, 'studentDashboard.html', {"r_block":r_block})
    else:
        if BH2.objects.filter(roll_1=roll_1).exists() or BH2.objects.filter(roll_2=roll_1).exists():
            print("Roll no 1 already allocated room")
            messages.info(request,"Room already allocated")
            r_block = check_room(roll_no,year,gender)
            return render(request, 'studentDashboard.html', {"r_block":r_block})

    if WaitingTable.objects.filter(roll_no=roll_1).exists():
        print('Roll no already in waiting table')
        messages.info(request,"Already in waiting table")
        r_block = check_room(roll_no,year,gender)
        return render(request, 'studentDashboard.html', {"r_block":r_block})

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

    r_block = check_room(roll_no,year,gender)
    return render(request, 'studentDashboard.html', {"r_block":r_block})

def contactUs(request):
    objs = CustomUser.objects.filter(user_type="2")
    objs1 = Warden.objects.all()
    return render(request, 'contactUs.html', {'objs': objs, 'objs1': objs1})

def viewComplain(request):
    complain = Complaint.objects.all()
    return render(request, 'viewComplain.html', {'complain': complain, 'user':CustomUser})

def studentList(request):
    warden=CustomUser.objects.get(id=request.user.id)
    block=Warden.objects.get(admin_id=warden.id).block_name
    if block.block_name=="GH1":
        student_list=Student.objects.filter(year=1,gender='Female')
        return render(request,'studentList.html',{'student_list':student_list, 'block':block})
    elif block.block_name=="GH2":
        student_list=Student.objects.filter(year=2,gender='Female')
        return render(request,'studentList.html',{'student_list':student_list, 'block':block})
    elif block.block_name=="GH3":
        student_list=Student.objects.filter(year=3,gender='Female')
        return render(request,'studentList.html',{'student_list':student_list, 'block':block})
    elif block.block_name=="GH4":
        student_list=Student.objects.filter(year=4,gender='Female')
        return render(request,'studentList.html',{'student_list':student_list, 'block':block})
    elif block.block_name=="BH1":
        student_list=Student.objects.filter(year=1,gender='Male')
        return render(request,'studentList.html',{'student_list':student_list, 'block':block})
    elif block.block_name=="BH2":
        student_list=Student.objects.filter(year=2,gender='Male')
        return render(request,'studentList.html',{'student_list':student_list, 'block':block})
    elif block.block_name=="BH3":
        student_list=Student.objects.filter(year=3,gender='Male')
        return render(request,'studentList.html',{'student_list':student_list, 'block':block})
    elif block.block_name=="BH4":
        student_list=Student.objects.filter(year=4,gender='Male')
        return render(request,'studentList.html',{'student_list':student_list, 'block':block})

def knowYourWarden(request):
    user=CustomUser.objects.get(id=request.user.id)
    student=Student.objects.get(admin_id=user.id)
    year=student.year
    gender=student.gender
    admin_id = request.user.id
    roll_no = student.roll_no
    r_block = check_room(roll_no,year,gender)
    if gender=='Male':
        if year==1:
            block='BH1'
            warden=Warden.objects.get(block_name=block)
            customUser=CustomUser.objects.get(id=warden.admin_id)
            return render(request, 'knowYourWarden.html',{'warden':warden, 'customUser':customUser, "r_block":r_block})
        elif year==2:
            block='BH2'
            warden=Warden.objects.get(block_name=block)
            customUser=CustomUser.objects.get(id=warden.admin_id)
            return render(request, 'knowYourWarden.html',{'warden':warden, 'customUser':customUser, "r_block":r_block})
        elif year==3:
            block='BH3'
            warden=Warden.objects.get(block_name=block)
            customUser=CustomUser.objects.get(id=warden.admin_id)
            return render(request, 'knowYourWarden.html',{'warden':warden, 'customUser':customUser, "r_block":r_block})
        elif year==4:
            block='BH4'
            warden=Warden.objects.get(block_name=block)
            customUser=CustomUser.objects.get(id=warden.admin_id)
            return render(request, 'knowYourWarden.html',{'warden':warden, 'customUser':customUser, "r_block":r_block})
    elif gender=='Female':
        if year==1:
            block='GH1'
            warden=Warden.objects.get(block_name=block)
            customUser=CustomUser.objects.get(id=warden.admin_id)
            return render(request, 'knowYourWarden.html',{'warden':warden, 'customUser':customUser, "r_block":r_block})
        elif year==2:
            block='GH2'
            warden=Warden.objects.get(block_name=block)
            customUser=CustomUser.objects.get(id=warden.admin_id)
            return render(request, 'knowYourWarden.html',{'warden':warden, 'customUser':customUser, "r_block":r_block})
        elif year==3:
            block='GH3'
            warden=Warden.objects.get(block_name=block)
            customUser=CustomUser.objects.get(id=warden.admin_id)
            return render(request, 'knowYourWarden.html',{'warden':warden, 'customUser':customUser, "r_block":r_block})
        elif year==4:
            block='GH4'
            warden=Warden.objects.get(block_name=block)
            customUser=CustomUser.objects.get(id=warden.admin_id)
            return render(request, 'knowYourWarden.html',{'warden':warden, 'customUser':customUser, "r_block":r_block})

        