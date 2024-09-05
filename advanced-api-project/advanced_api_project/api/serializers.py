from django.db import models
from rest_framework import serializers
from models import Author, Book
from datetime import datetime

class BookSerializer(serializers.Serializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']
    pass

class AuthorSerialzer(serializers.Serializer):
    class Meta:
        model = Author
        fields = ['name']
        
        class BookSerializer(BookSerializer):
            publication_year = datetime.now
            