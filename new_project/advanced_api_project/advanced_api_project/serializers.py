from django.db import models
from rest_framework import serializers
from api.models import Author, Book

class BookSerializer(serializers.Serializer):
    model = Book
    fields = ['title', 'publication_year', 'author']


class AuthorSerializer(serializers.Serializer):
    model = Author
    fields = ['name']