from django.db import models

# Create your models here.

class Author ():
    name = models.CharField()

class Book ():
    title = models.CharField()
    author = models.ForeignKey(Author)
    
class Library ():
    name = models.CharField()
    books = models.ManyToManyField(Book)

class Librarian ():
    name = models.CharField
    library = models.ManyToManyField(Library)
