from django.shortcuts import render
from django_filters import rest_framework
from rest_framework import generics, filters
from .models import Book, Author
from .serializers import AuthorSerializer, BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser


class CustomBookListView(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [filters.OrderingFilter], [filters.SearchFilter]
    serach_fields = ['title', 'author', 'publication_year']
    

class CustomBookDetailView(generics.DetailAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class CustomBookCreateView(generics.CreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class CustomBookUpdateView(generics.UpdateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class CustomBookDeleteView(generics.DeleteAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
