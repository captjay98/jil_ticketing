from django.http import HttpResponse
from django.shortcuts import render

from .models import *

# Create your views here.

def home(request):
    return render(request, 'main.html')
    #return HttpResponse("JIL TICKETING")

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

def schedule(request):
    return render(request, 'schedule.html')
