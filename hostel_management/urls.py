from django.urls import path
from . import views
from django.contrib import admin

admin.site.site_header = "Hostel Management System"
admin.site.site_title = "Hostel Managment System Admin"
admin.site.site_index = "Welcome to the portal!"

urlpatterns = [
    path('home', views.home, name="home"),
    path('register', views.register, name="register"),
    path('registerWarden', views.registerWarden, name="registerWarden"),
    path('signin', views.signin, name="signin"),
    path('warden', views.signinwarden, name="signinwarden"),
    path('dosigninWarden', views.dosigninWarden, name="dosigninWarden"),
    path('dosigninStudent', views.dosigninStudent, name="dosigninStudent"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('register_form_submission', views.register_form_submission,
         name="register_form_submission"),
    path('room_register2', views.room_register2, name="room_register2"),
    path('room_register_2', views.room_register_2, name="room_register_2"),
    path('room_register134', views.room_register134, name="room_register134"),
    path('room_register_1_3_4', views.room_register_1_3_4,
         name="room_register_1_3_4"),
    path('waiting_table_form', views.waiting_table_form, name="waiting_table_form"),
    path('waiting_table', views.waiting_table, name="waiting_table"),
    path('registerWarden_form_submission', views.registerWarden_form_submission,
         name="registerWarden_form_submission"),
    path('contactUs', views.contactUs, name="contactUs"),
    path('complainForm', views.complainForm, name="complain"),
    path('complainFormSubmission', views.complainFormSubmission,
         name="complainFormSubmission"),
    path('signout', views.dosignout, name="dosignout"),
    path('wardenDashboard', views.wardenDashboard, name="wardenDashboard"),
    path('viewComplain', views.viewComplain, name="viewComplain"),
     path('studentList', views.studentList, name="studentList"),
     path('knowYourWarden',views.knowYourWarden, name="knowYourWarden"),
     path('roomAllocation', views.roomAllocation, name="roomAllocation"),
     path('form_roomAllocation',views.form_roomAllocation,name="form_roomAllocation")
]
