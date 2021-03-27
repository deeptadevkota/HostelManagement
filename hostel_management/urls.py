from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('register', views.register, name="register"),
    path('signin', views.signin, name="signin"),
    path('warden', views.signinwarden, name="signinwarden"),
    path('dosigninWarden', views.dosigninWarden, name = "dosigninWarden"),
    path('dosigninStudent', views.dosigninStudent, name = "dosigninStudent"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('register_form_submission', views.register_form_submission,
         name="register_form_submission"),
    path('room_register2', views.room_register2, name = "room_register2"),
    path('room_register_2', views.room_register_2, name = "room_register_2"),
    path('room_register134', views.room_register134, name = "room_register134"),
    path('room_register_1_3_4', views.room_register_1_3_4, name = "room_register_1_3_4"),
    path('waiting_table_form',views.waiting_table_form, name = "waiting_table_form"),
    path('waiting_table',views.waiting_table, name = "waiting_table")
]
