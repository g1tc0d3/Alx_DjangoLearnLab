from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User (AbstractUser):
    pass

class Post(models.Model):
    title=models.CharField(max_length=250)
    content=models.TextField()
    published_date=models.DateTimeField(auto_now_add=True)
    # author=models.ForeignKey(on_delete=models.CASCADE)

class Comment (models.Model):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(User)
    content = models.TextField
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
