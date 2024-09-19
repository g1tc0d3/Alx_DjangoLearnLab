from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser (AbstractUser):
    pass

class Post(models.Model):
    title=models.CharField(max_length=250)
    content=models.TextField()
    published_date=models.DateTimeField(auto_now_add=True)
    # author=models.ForeignKey(on_delete=models.CASCADE)

