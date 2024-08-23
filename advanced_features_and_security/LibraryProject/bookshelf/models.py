from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class Books ():
    title = models.CharField (max_length= 200)
    author = models.CharField (max_length= 100)
    publication_year = models.IntegerField ()
    

class CustomUser(AbstractBaseUser):
    date_of_birth = models.DateField
    profile_photo = models.ImageField

    