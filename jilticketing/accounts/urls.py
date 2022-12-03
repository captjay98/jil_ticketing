from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("register", views.RegisterView, name="registration"),
    path("login", views.LoginView, name="login"),
    path("logout",views.LogoutView, name="logout"),
    path("profile", views.ProfileView, name="profile"),
    path("trip", views.TripView, name="trip"),
    path("trips", views.TripsView, name="trips"),
    path("book", views.BookingView, name="book"),
    path("confirm", views.ConfirmView, name="confirm"),
    path("seat", views.SeatView, name="seat"),
]
