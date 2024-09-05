from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=250)
    pass

class Book(models.Model):
    title = models.CharField
    publication_year = models.IntegerField
    author = models.ForeignKey(Author)
    pass


