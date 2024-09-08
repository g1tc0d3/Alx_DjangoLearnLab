from django.test import testcases
from rest_framework.test import APITestCase
from api.models import Book

class BookTestCase(TestCase):
    def setup (self):
        Book.objects.create()
        Book.objects.order()
        Book.objects.filter()
        Book.objects.search()
