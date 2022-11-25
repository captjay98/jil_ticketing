from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import Booking, Ticket, TicketType, Trip, User

# Create your views here.


@login_required(login_url='login')
def home(request):
    """
    Returns the Homescreen only
    available to logged in users
    """
    # name = User.objects.all()
    return render(request, 'accounts/home.html')


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
        return render(request, 'accounts/register.html')


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
        return render(request, 'accounts/login.html')


@login_required(login_url='login')
def LogoutView(request):
    """
    logs out the active user
    Args:
        request (request): a user request
    Returns:
        redirect: a user to the homepage
    """
    logout(request)
    return redirect("home")


@login_required(login_url='login')
def ProfileView(request):
    """
    displays user information
    and previous bookings
    plus current if there is any.

    Returns:
        render: a page with the user information
    """
    user = request.user
    bookings = Booking.objects.filter(user_id=user.id)

    context = {'bookings': bookings, 'user': user}

    return render(request, 'accounts/profile.html', context)


def ScheduleView(request):
    """
    Displays the schedule
    and allows user to choose
    their trip`
    """
    trips = Trip.objects.all()
    context = {"trips": trips}

    if request.method == 'POST':
        trip_choice = request.POST.get('trip')
        trip_choice = int(trip_choice)

        request.session['trip'] = trip_choice
        print("TRIP CHOICE ID IS", trip_choice, type(trip_choice))
        messages.success(request, "Select a Ticket Type")
        return redirect('book')

    return render(request, 'accounts/trips.html', context)


"""
def SeatCheck(trip, ticket, seattype):
    if trip == trip:
        if ticket % 2 != 0:
            if seattype == 11:
                print("Sorry we are out of Economy Tickets")
            else:
                seattype += 1
                seat = seattype

        elif ticket % 2 == 0:
            if seattype == 6:
                print("Sorry we are out of Business Tickets")
            else:
                seattype += 1
                seat = seattype
    return seat
"""


@login_required(login_url='login')
def BookingView(request):
    """
    Books a ticket of choice
    for the user
    """
    trip_choice = request.session.get('trip')
    trip_choice = int(trip_choice)

    tickettypes = TicketType.objects.filter(trip_id=trip_choice)

    if request.method == 'POST':
        ticket_choice = request.POST.get('tickettype')
        ticket_choice = int(ticket_choice)
        request.session['ticket'] = ticket_choice
        # hhgayixx pwcu rdrc

        if trip_choice == 3:
            if ticket_choice % 2 != 0:
                if Ticket.kdEconomy == 11:
                    messages.info(request,
                                  "Sorry, We are Out of Economy Tickets")
                else:
                    Ticket.kdEconomy += 1
                    seat = Ticket.kdEconomy

            elif ticket_choice % 2 == 0:
                if Ticket.kdBusiness == 6:
                    messages.info(request,
                                  "Sorry, We are Out of Business Tickets")
                Ticket.kdBusiness += 1
                seat = Ticket.kdBusiness
            else:
                messages.info(request, "Invalid Ticket Code")

        elif trip_choice == 4:
            if ticket_choice % 2 != 0:
                if Ticket.knEconomy == 11:
                    messages.info(request,
                                  "Sorry, We are Out of Economy Tickets")
                else:
                    Ticket.knEconomy += 1
                    seat = Ticket.knEconomy

            elif ticket_choice % 2 == 0:
                if Ticket.knBusiness == 6:
                    messages.info(request,
                                  "Sorry, We are Out of Business Tickets")
                Ticket.knBusiness += 1
                seat = Ticket.knBusiness
            else:
                messages.info(request, "Invalid Ticket Code")
        else:
            messages.info(request, "Invalid Trip")

        print("TICKET TYPE ID IS :", request.session['ticket'],
              type(ticket_choice))

        ticket = Ticket.objects.create(ticket_type_id=ticket_choice,
                                       trip_id=trip_choice,
                                       seat=seat)
        ticket.save()

        booking = Booking.objects.create(user_id=request.user.id,
                                         ticket_id=ticket.id)

        booking.save()
        messages.success(request, "Please confirm your booking info and"
                         " download ticket")
        return redirect("confirm")

    context = {"tickettypes": tickettypes}
    return render(request, 'accounts/book.html', context)


@login_required(login_url='login')
def ConfirmView(request):
    """
    Shows the booking information
    """
    ticketclass = request.session.get('ticket')
    ticketclass = int(ticketclass)
    tripchoice = request.session.get('trip')
    tripchoice = int(tripchoice)

    print("TICKETCLASS ID", ticketclass, type(ticketclass))
    print("TRIPCHOICE ID:", tripchoice, type(tripchoice))
    # filter the bookings by ascendig order and pick out the latest
    # ticketconfirm = Ticket.objects.all() "ticketconfirmation": ticketconfirm,
    bookingconfirm = Booking.objects.filter(user_id=request.user.id)

    context = {"bookingconfirmation": bookingconfirm}

    return render(request, 'accounts/confirm.html', context)
