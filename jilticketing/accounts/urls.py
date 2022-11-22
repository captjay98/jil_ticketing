from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("register", views.RegisterView, name="registration"),
    path("login", views.LoginView, name="login"),
    path("profile", views.ProfileView, name="profile"),
    path("trips", views.ScheduleView, name="trips"),
    path("book", views.BookingView, name="book"),
    path("confirm", views.ConfirmView, name="confirm"),
]
