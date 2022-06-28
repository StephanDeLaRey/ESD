from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,AbstractUser
from django.utils.translation import gettext_lazy as _
import random




# Create your models here.
class UserManager(BaseUserManager):


    def create_user(self, email, password, **extra_fields):

        """

        Create and save a User with the given email and password.

        """

        if not email:

            raise ValueError(_('The Email must be set'))

        email = self.normalize_email(email)

        extra_fields.setdefault('is_staff', False)

        extra_fields.setdefault('is_superuser', False)

        extra_fields.setdefault('is_active', True)
        

        user = self.model(email=email, **extra_fields)

        user.set_password(password)
       # user.phone_number=phone_number
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):

        """

        Create and save a SuperUser with the given email and password.

        """

        extra_fields.setdefault('is_staff', True)

        extra_fields.setdefault('is_superuser', True)

        extra_fields.setdefault('is_active', True)



        if extra_fields.get('is_staff') is not True:

            raise ValueError(_('Superuser must have is_staff=True.'))

        if extra_fields.get('is_superuser') is not True:

            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):

    username = None

    first_name = models.CharField(null=False, max_length=255)

    last_name = models.CharField(null=False, max_length=255)

    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = UserManager()



    def __unicode__(self):

        return self.first_name + ' ' + self.last_name



    def __str__(self):

        return self.email



    def get_full_name(self):

        return self.first_name + ' ' + self.last_name