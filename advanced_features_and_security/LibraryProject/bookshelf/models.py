from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.contrib.auth.models import BaseUserManager 


# Create your models here.
class Books (models.Model):
    title = models.CharField (max_length= 200)
    author = models.CharField (max_length= 100)
    publication_year = models.IntegerField ()
    can_create = models.CharField
    can_delete = models.CASCADE
    

class CustomUser(AbstractUser):
    date_of_birth = models.DateField
    profile_photo = models.ImageField

class CustomUserManager(BaseUserManager):
    def create_user():
        pass

    def create_superuser():
        pass

class CustomUserAdmin():
    pass

