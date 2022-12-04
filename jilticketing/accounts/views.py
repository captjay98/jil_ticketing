from http.client import HTTPResponse
from unicodedata import name

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms import ValidationError
from django.shortcuts import redirect, render

from .models import Booking, Ticket, TicketType, Trip, User

# Create your views here. okay


def home(request):
    """
    Returns the Homescreen only
    available to logged in users
    """

    user = request.user
    trips = Trip.objects.all()
    context = {"trip": trips}

    if user.is_authenticated:
        if request.method == "POST":
            departure = request.POST.get("departure")
            destination = request.POST.get("destination")
            date = request.POST.get("date")

            print("DEPARTURE::", departure)
            print("DESTINATION::", destination)
            print("DATE::", date)

            request.session["departure"] = departure
            request.session["destination"] = destination
            request.session["date"] = date

            return redirect("trip")

        return render(request, "accounts/reghome.html", context)
    else:
        if request.method == "POST":
            departure = request.POST.get("departure")
            destination = request.POST.get("destination")
            date = request.POST.get("date")

            print("DEPARTURE::", departure)
            print("DESTINATION::", destination)
            print("DATE::", date)

            request.session["departure"] = departure
            request.session["destination"] = destination
            request.session["date"] = date

            return redirect("trip")
        return render(request, "accounts/home.html")


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
        username = request.POST["username"]
        email = request.POST["email"]
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
                user = user.objects.create_user(
                    first_name=first_name,
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
            messages.info(request, "Passwords Do Not Match!")
            return redirect("registration")

    else:
        return render(request, "accounts/register.html")


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
        return render(request, "accounts/login.html")


@login_required(login_url="login")
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


@login_required(login_url="login")
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

    context = {"bookings": bookings, "user": user}

    return render(request, "accounts/profile.html", context)


def TripView(request):
    """
    Displays the schedule
    and allows user to choose
    their trip`
    """

    trips = Trip.objects.all()
    context = {"trips": trips}

    try:
        departure = request.session.get("departure").capitalize()
        destination = request.session.get("destination").capitalize()
        date = request.session.get("date")

        print("DEPARTURE::", departure)
        print("DESTINATION::", destination)
        print("DATE::", date)
        if departure == "":
            messages.error(request, "Enter a Valid Departure Venue")
            return redirect("home")
        elif destination == "":
            messages.error(request, "Enter a Valid Destination Venue")
            return redirect("home")
        trips = Trip.objects.filter(
            departure=departure, destination=destination, date=date
        )
        context = {"trips": trips}

    except ValidationError:
        messages.error(request, "Enter a Valid Trip Date")
        return redirect("home")

    if request.method == "POST":
        trip_choice = request.POST.get("trip")

        if trip_choice is not None:
            trip_choice = int(trip_choice)

            request.session["trip"] = trip_choice
            print("TRIP CHOICE ID IS", trip_choice, type(trip_choice))
            messages.success(request, "Select a Ticket Type")
            return redirect("book")
        else:
            messages.error(request, "Please Select a Trip")

    return render(request, "accounts/trip.html", context)


def TripsView(request):
    trips = Trip.objects.all()
    context = {"trips": trips}

    if request.method == "POST":
        trip_choice = request.POST.get("trip")

        if request.user.is_authenticated == False:
            messages.error(request, "Sorry. You have to login before booking. ")
            return redirect("login")

        elif trip_choice is not None:
            trip_choice = int(trip_choice)

            request.session["trip"] = trip_choice
            print("TRIP CHOICE ID IS", trip_choice, type(trip_choice))
            messages.success(request, "Select a Ticket Type")
            return redirect("book")
        else:
            messages.error(request, "Please Select a Trip")

    return render(request, "accounts/trips.html", context)


"""
def SeatView(request, trip, seattype):
    availableSeats = 2  # [1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,]

    if seattype == "business":
        for seat in availableSeats:

            if availableSeats[seat] == 1:
                bookseat = availableSeats.index("availableseats")
                availableSeats[seat] = 0
                return bookseat
            else:
                messages.info(request, "NO Available Seats")

    elif seattype == "economy":
        for seat in availableSeats:

            if availableSeats[seat] == 2:
                bookseat = availableSeats.index("availableseats")
                availableSeats[seat] = 0
                return bookseat
            else:
                messages.info(request, "NO Available Seats")

    else:
        messages.info(request, "Invalid Ticket Type")

    return render(request, "accounts/seat.html")


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
    
    create seats
    [11O11
    11O11
    11O11
    11O11
    11O11]
    sit = seat[1]
    seat[1] = x
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
"""


@login_required(login_url="login")
def BookingView(request):
    """
    Books a ticket of choice
    for the user
    """
    trip_choice = request.session.get("trip")
    trip_choice = int(trip_choice)

    tickettypes = TicketType.objects.filter(trip_id=trip_choice)

    if request.method == "POST":
        ticket_choice = request.POST.get("tickettype")

        ticket_choice = ticket_choice.split(" ")
        ticket_choice_id = ticket_choice[0]
        ticket_choice_class = ticket_choice[1].lower()
        request.session["ticket_choice_id"] = ticket_choice_id
        request.session["ticket_choice_class"] = ticket_choice_class
        print(ticket_choice)

        if ticket_choice is None:
            messages.error(request, "Please Select a Ticket")
        else:
            return redirect("payment")
    else:
        return HTTPResponse("<h1> Payment Failed </h1>")

    context = {"tickettypes": tickettypes}
    return render(request, "accounts/book.html", context)


def PayView(request):
    """
    Allows users to make payments
    via a debit or Credit Card
    """
    if request.method == "POST":

        trip_choice = request.session.get("trip")
        ticket_choice_id = request.session.get("ticket_choice_id")
        ticket_choice_class = request.session.get("ticket_choice_class")

        trip_choice = int(trip_choice)
        ticket_choice_id = int(ticket_choice_id)

        tc = Ticket.objects.filter(trip=trip_choice)
        bc = Ticket.objects.filter(trip=trip_choice, ticket_type=ticket_choice_id)

        if ticket_choice_class == "economy":
            if tc.count == 11:
                messages.info("Sorry, We are out of Economy class tickets.")
            else:
                seat = 20 - tc.count() - bc.count()

        elif ticket_choice_class == "business":
            if tc.count == 10:
                messages.info("Sorry, We are out of Business class tickets.")
            else:
                seat = tc.count() + 1

        ticket = Ticket.objects.create(
            ticket_type_id=ticket_choice_id, trip_id=trip_choice, seat=seat
        )
        ticket.save()

        booking = Booking.objects.create(user_id=request.user.id, ticket_id=ticket.id)

        booking.save()

        return redirect("confirm")
    return render(request, "accounts/pay.html")


@login_required(login_url="login")
def ConfirmView(request):
    """
    Shows the last booking information
    if not before trip date
    """

    if request.method == "GET":
        bookingconfirm = Booking.objects.filter(user_id=request.user.id).order_by(
            "-id"
        )[:1]

        context = {"bookingconfirmation": bookingconfirm}

        return render(request, "accounts/confirm.html", context)

    else:
        return HTTPResponse(
            "<h1>You do not have an active booking,\
                            Please visit your profile\
                            and check previous Bookings.</h1>"
        )


def Download(request):

    # create the logic to download a ticket
    pass
