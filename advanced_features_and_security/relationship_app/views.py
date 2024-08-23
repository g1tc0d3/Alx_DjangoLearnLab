from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library
from .models import relationship_app
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import permission_required

# Create your views here.

"relationship_app/list_books.html", "Book.objects.all()"

"relationship_app/library_detail.html", "Library"

"relationship_app.can_add_book", "relationship_app.can_delete_book", "relationship_app.can_change_book",


