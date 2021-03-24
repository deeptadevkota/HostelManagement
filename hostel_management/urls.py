from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('register', views.register, name="register"),
    path('registerWarden', views.registerWarden, name="registerWarden"),
    path('signin', views.signin, name="signin"),
    path('warden', views.signinwarden, name="signinwarden"),
    path('dosigninWarden', views.dosigninWarden, name = "dosigninWarden"),
    path('dosigninStudent', views.dosigninStudent, name = "dosigninStudent"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('register_form_submission', views.register_form_submission,
         name="register_form_submission"),
    path('registerWarden_form_submission', views.registerWarden_form_submission,
         name="registerWarden_form_submission"),
    path('contactUs', views.contactUs, name="contactUs")
]
