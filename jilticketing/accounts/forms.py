from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import User, Trip, TicketType, Departure, Destination

'''
class RegistrationForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField(help_text="Enter a Valid Usernae")
    email = forms.EmailField(
                widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    phone_number = forms.CharField(help_text="+234")
    date_of_birth = forms.DateField()
    state = forms.CharField()

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username",
                  "email", "phone_number", "state",
                  "date_of_birth", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        try:
            user = User.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"Email {email} is taken")

    def clean_username(self):
        username = self.cleaned_data["username"].lower()
        try:
            user = User.objects.get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"username {username} is taken")


class UserAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label="password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("email", "password")

    def clean(self):
            if self.is_valid():
                email = self.cleaned_data["email"]
                password = self.cleaned_data["password"]
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid Login")
'''


class BookingForm(forms.Form):
    trips = Trip.objects.all()
    tickettype = TicketType.objects.all()

    ticket_choice = forms.ChoiceField(choices=tickettype, required=True)
    trip_choice = forms.ChoiceField(choices=trips, required=True)
