from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import (Booking, Ticket, TicketType, Trip,
                     User)

# Create your views here.


@login_required(login_url='login')
def home(request):
    """
    Returns the Homescreen only
    available to logged in users
    """
    # name = User.objects.all()
    return render(request, 'main.html')


def RegisterView(request):
    """
    Registers New user
    """
    user = User
    """
    if user.is_authenticated:
        return HttpResponse(f"You are already authenticated as {user.email}")
    """
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST['username']
        email = request.POST['email']
        phone_number = request.POST["phone_number"]
        state = request.POST["state"]
        date_of_birth = request.POST["date_of_birth"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            if user.objects.filter(email=email).exists():
                messages.info(request, f"Email {email} already in use")
                return redirect("registration")

            elif user.objects.filter(username=username).exists():
                messages.info(request, f"Username {username} is taken")
                return redirect("registration")

            elif user.objects.filter(phone_number=phone_number).exists():
                messages.info(request, f"Phone number {phone_number} is taken")
                return redirect("registration")

            else:
                user = user.objects.create_user(first_name=first_name,
                                                last_name=last_name,
                                                username=username,
                                                email=email,
                                                phone_number=phone_number,
                                                state=state,
                                                date_of_birth=date_of_birth,
                                                password=password1,
                                                )
                user.save()
                user = authenticate(email=email, password=password1)
                login(request, user)
                return redirect("home")
        else:
            messages.info(request, 'Passwords Do Not Match!')
            return redirect("registration")

    else:
        return render(request, 'register.html')


def LoginView(request):

    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, "Incorrect email or password")
            return redirect("login")
    else:
        return render(request, 'login.html')


@login_required(login_url='login')
def LogoutView(request):
    logout(request)
    return redirect("home")


@login_required(login_url='login')
def ProfileView(request):
    """
    displays user information
    and previous bookings
    plus current if there is any.
    """
    user = request.user
    bookings = Booking.objects.filter(user_id=user.user_id)

    context = {'bookings': bookings, 'user': user}

    return render(request, 'profile.html', context)


def ScheduleView(request):
    trips = Trip.objects.all()
    context = {"trips": trips}

    if request.method == 'POST':
        trip_choice = request.POST.get('trip')
        trip_choice = int(trip_choice)

        request.session['trip'] = trip_choice
        print("TRIP CHOICE ID IS", trip_choice, type(trip_choice))
        messages.success(request, "Select a Ticket Type")
        return redirect('book')

    return render(request, 'trips.html', context)


def TripChoiceView(request):
    pass


def TicketChoiceView(request):
    pass


@login_required(login_url='login')
def BookingView(request):
    trip_choice = request.session.get('trip')
    trip_choice = int(trip_choice)

    tickettypes = TicketType.objects.filter(trip_id=trip_choice)

    if request.method == 'POST':
        ticket_choice = request.POST.get('tickettype')
        ticket_choice = int(ticket_choice)
        request.session['ticket'] = ticket_choice

        print("TICKET TYPE ID IS :", request.session['ticket'],
              type(ticket_choice))

        ticket = Ticket.objects.create(ticket_type_id=ticket_choice,
                                       trip_id=trip_choice)
        ticket.save()

        booking = Booking.objects.create(user_id=request.user.id,
                                         ticket_id=ticket.id)

        booking.save()
        messages.success(request, "Please confirm your booking info and"
                         " download ticket on the next page")
        return redirect("confirm")

    context = {"tickettypes": tickettypes}
    return render(request, 'book.html', context)


@login_required(login_url='login')
def ConfirmView(request):
    ticketclass = request.session.get('ticket')
    ticketclass = int(ticketclass)
    tripchoice = request.session.get('trip')
    tripchoice = int(tripchoice)

    print("TICKETCLASS ID", ticketclass, type(ticketclass))
    print("TRIPCHOICE ID:", tripchoice, type(tripchoice))

    ticketconfirm = Ticket.objects.all()
    bookingconfirm = Booking.objects.all()

    context = {"ticketconfirmation": ticketconfirm,
               "bookingconfirmation": bookingconfirm}

    return render(request, 'confirm.html', context)

    """

    ticket_choice = request.GET.get('ticket_choice')
    trip_choice = request.GET.get('trip_id')

    tickettype = TicketType.objects.filter(seat_class=ticket_choice,
                                           trip_id=trip_choice)

    trip = Trip.objects.filter(location=trip_choice)

    ticket = Ticket.objects.create(user_id=request.user,
                                   seat_class=tickettype,
                                   )
    ticket.save()
    booking = Booking.objects.create(user_id=request.user)
    booking.save(

        )
    if request.method == 'POST':
        ticket = request.POST.get("Ticket")
        day = request.POST.get("day")
        depart = request.POST.get("depart")
        arrive = request.POST.get("arrive")


        request.session["day"] = day
        request.session["ticket"] = ticket
        request.session["depart"] = depart
        request.session["arrive"] = arrive
        '''
    return HttpResponse(booking)
    """
