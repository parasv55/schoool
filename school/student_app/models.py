
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import ForeignKey
from django.shortcuts import reverse
from django.core.validators import RegexValidator
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.




class AuthUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    Mobile_Number = models.CharField(max_length=10, validators=[
                                     RegexValidator(r'^\d{10}$')])
    Address = models.CharField(max_length=200)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=20)
    bio = models.CharField(max_length=80, null=True, blank=True)
    Pincode = models.CharField(max_length=6, validators=[
        RegexValidator(r'^\d{6}$')])
    image = models.ImageField(upload_to='profile_images', null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []    

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

class Demo(models.Model):
    image = models.ImageField(upload_to = 'profile_images', null = True, blank = True)