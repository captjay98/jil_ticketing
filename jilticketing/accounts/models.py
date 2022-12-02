from datetime import time
from uuid import uuid4

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.forms import CharField

# from django.conf import settings


def default_profile_image_path(self):
    return f"profile_images/{self.pk}/{'profile_image'}"


def default_profile_image(self):
    return "default_images/default_image.png"


# Create your models here.
class MyAccountManager(BaseUserManager):

    def create_user(self, first_name, last_name, email, username,
                    phone_number, date_of_birth, state, password=None):
        if not email:
            raise ValueError("Email Required")
        if not username:
            raise ValueError("Username Required  ")
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            username=username,
            phone_number=phone_number,
            date_of_birth=date_of_birth,
            state=state
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """
    A custom User class
    derived from Abstract Base User
    uses the  EMAIL for login
    instead of username
    """
    first_name      = models.CharField(verbose_name="first name",
                                       max_length=50)
    last_name       = models.CharField(verbose_name="last name", max_length=50)
    username        = models.CharField(verbose_name="username",
                                       max_length=50, unique=True)
    email           = models.EmailField(verbose_name="email",
                                        max_length=50, unique=True)
    phone_number    = models.CharField(verbose_name="phone number",
                                       max_length=50, blank=True,
                                       null=True, unique=True)
    date_of_birth   = models.DateField(verbose_name='Date of Birth',
                                       null=True, blank=True)
    state           = models.CharField(verbose_name="state", max_length=50)

    date_joined     = models.DateTimeField(verbose_name="date joined",
                                           auto_now_add=True)
    last_login      = models.DateField(verbose_name="last login",
                                       auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    hide_email      = models.BooleanField(default=True)
    # profile_image = models.ImageField(max_length=255, blank=True,
    # null=True, upload_to=, default=default_profile_image_path )

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.first_name + ' ' + self.last_name
        # self.username

    '''def profile_image_filename(self):
        return str(self.profile_image)
         [str(self.profile_image).index(f"profile_images/{self.pk}/"):]
    '''

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

# User = settings.AUTH_USER_MODEL


class Booking(models.Model):
    """
    Defines the Booking Table
    """
    user = models.ForeignKey('User', related_name='users',
                             on_delete=models.DO_NOTHING)
    ticket = models.ForeignKey('Ticket', related_name='tickets',
                               on_delete=models.DO_NOTHING)
    # delivery_email = models.ForeignKey()

    def __str__(self):
        return f"{self.user}  {self.ticket}"


class Ticket(models.Model):
    """
    Defines the ticket Table
    """
    serial_number = models.UUIDField(default=uuid4)
    generated_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    seat = models.IntegerField()
    ticket_type = models.ForeignKey('TicketType',
                                    related_name='ticket_types',
                                    on_delete=models.DO_NOTHING)
    trip = models.ForeignKey('Trip', related_name='trips',
                             on_delete=models.DO_NOTHING)
    
    kdBusiness = 0
    kdEconomy = 5
    
    knBusiness = 0
    knEconomy = 5


    def __str__(self):
        return (f"{self.trip.departure} to {self.trip.destination}\
                {self.ticket_type.seat_class} {self.id}")


class TicketType(models.Model):
    """
    Defines the Ticket Types table
    """
    # name = models.CharField(max_length=50)
    id = models.AutoField(primary_key=True)
    seat_class = models.CharField(max_length=50)
    price = models.IntegerField()
    trip = models.ForeignKey('Trip', related_name='trip',
                             on_delete=models.DO_NOTHING)

   
    def __str__(self):
        return f"{str(self.id)} {self.trip.departure} to {self.trip.destination}\
            {self.seat_class}"


class Trip(models.Model):
    """
    Defines the Trips table
    """
    name = models.CharField(max_length=50)
    date = models.DateField()
    departure = models.CharField(max_length=50)
    departure_time = models.TimeField(default='00:00:00')
    destination = models.CharField(max_length=50)
    arrival_time = models.TimeField(default='00:00:00')

    def __str__(self):
        return f"{self.id} {self.departure}  to  {self.destination}"