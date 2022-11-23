from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (Booking, Departure, Destination, Ticket, TicketType, Trip,
                     User)

# Register your models here.


class User_Admin(UserAdmin):
    list_display = ("id", "username", "email", "first_name", "last_name",
                    "phone_number",  "date_of_birth", "state",
                    "date_joined", "last_login", "is_admin", "is_staff")
    search_fields = ("id", "email", "username", "phone_number", )
    readonly_fields = ("id", "date_joined", "last_login",)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
 
 
admin.site.register(User, User_Admin)   


class Booking_Admin(admin.ModelAdmin):
    list_display = ("id", "user", "ticket")
    search_fields = ("id", "user", "ticket")


admin.site.register(Booking, Booking_Admin)


class Ticket_Admin(admin.ModelAdmin):
    list_display = ("id", "ticket_type", "seat", "trip",
                    "generated_at", "expires_at", "serial_number")
    search_fields = ("serial_number", "ticket_type", "trip")


admin.site.register(Ticket, Ticket_Admin)


class TicketType_Admin(admin.ModelAdmin):
    list_display = ("id", "trip", "seat_class", "price")
    search_fields = ("id", "trip", "seat_class", "price")


admin.site.register(TicketType, TicketType_Admin)


class Trip_Admin(admin.ModelAdmin):
    list_display = ("id", "name", "date", "departure", "destination")
    search_fields = ("id", "name", "date", "departure", "destination")
    
admin.site.register(Trip, Trip_Admin)

class Departure_Admin(admin.ModelAdmin):
    list_display = ("id", "location", "departure_time")
    search_fields = ("id", "location", "departure_time")

admin.site.register(Departure, Departure_Admin)


class Destination_Admin(admin.ModelAdmin):
    list_display = ("id", "location", "arrival_time")
    search_fields = ("id", "location", "arrival_time")

admin.site.register(Destination, Destination_Admin)
