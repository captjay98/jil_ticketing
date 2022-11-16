from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

#from django.conf import settings

#from uuid import uuid4


def default_profile_image_path(self):
    return f"profile_images/{self.pk}/{'profile_image'}"

def default_profile_image(self):
    return "default_images/default_image.png"


# Create your models here.
class MyAccountManager(BaseUserManager):

    def create_user(self, first_name, last_name, email, username,
                    phone_number, date_of_birth, state , password=None):
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
            date_of_birth= date_of_birth,
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
    first_name      = models.CharField(verbose_name="first name" ,max_length=50)
    last_name       = models.CharField(verbose_name="last name", max_length=50)
    username        = models.CharField(verbose_name="username", max_length=50, unique=True)
    email           = models.EmailField(verbose_name="email", max_length=50, unique=True)
    phone_number    = models.CharField(verbose_name="phone number", max_length=50, blank=True, null=True, unique=True)
    date_of_birth   = models.DateField(verbose_name='Date of Birth', null=True, blank=True)
    state           = models.CharField(verbose_name="state", max_length=50)
    
    date_joined     = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login      = models.DateField(verbose_name="last login", auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    hide_email      = models.BooleanField(default=True)
    #profile_image = models.ImageField(max_length=255, blank=True, null=True, upload_to=, default=default_profile_image_path )
    
    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
        #self.username
    
    
    def profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index(f"profile_images/{self.pk}/"):]
        
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
     
#User = settings.AUTH_USER_MODEL