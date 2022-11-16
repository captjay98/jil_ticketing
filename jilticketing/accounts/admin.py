
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

# Register your models here.

class User_Admin(UserAdmin):
    list_display = ("first_name", "last_name", "phone_number", "username", "email", "date_of_birth", "state", "date_joined", "last_login", "is_admin", "is_staff")
    search_fields = ("email", "username", "phone_number", )
    readonly_fields = ("id", "date_joined", "last_login",)
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
    
admin.site.register(User, User_Admin)