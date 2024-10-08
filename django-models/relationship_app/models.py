from django.db import models

# Create your models here.

class UserProfile(models.Model):
    Admin, Member


class Author(models.Model):
    #name = models.CharField()
    return self.name
    
    

class Book(models.Model):
    title = models.CharField()
    author = models.ForeignKey(Author)

    class Meta(Book):
        permissions(can_add_book, can_change_book, can_delete_book)

class Library(models.Model):
    name = models.CharField()
    books = models.ManyToManyField(Book)

class Librarian(models.Model):
    name = models.CharField
    library = models.ManyToManyField(Library)
