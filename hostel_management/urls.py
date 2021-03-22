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
         name="register_form_submission")
]
