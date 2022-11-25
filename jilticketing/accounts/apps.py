from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"


"""def SeatCheck(request, trip_choice, ticket_choice):
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
                              "Sorry, We are Out of Economy Tickets")
                Ticket.kdBusiness += 1
                seat = Ticket.kdBusiness
        else:
            messages.info(request, "Invalid Ticket Code")
    return seat
"""
