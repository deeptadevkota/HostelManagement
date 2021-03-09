from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name = "home"),
    path('register', views.register, name ="register"),
    path('signin', views.signin, name ="signin"),
    path('warden', views.signinwarden, name = "signinwarden"),
    path('dashboard', views.dashboard, name = "dashboard")
]