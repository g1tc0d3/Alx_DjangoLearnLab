from django.test import TestCase
from api.models import Book

class BookTestCase(TestCase):
    def setup (self):
        Book.objects.create()
        Book.objects.order()
        Book.objects.filter()
        Book.objects.search()
        