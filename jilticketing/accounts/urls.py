from sched import scheduler
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home")
    path("/register", views.register, name="registration")
    path("/login", views.login, name="login")
    path("/profile", views.profile, name="profile")
    path("/schedule", views.schedule, name="schedules")
]
