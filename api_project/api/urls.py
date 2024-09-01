from django.urls import path, include
from views import BookListCreateAPIView, BookViewSets
from rest_framework.routers import DefaultRouter
from .models import Book

router=DefaultRouter()
router.register(r'my-models', BookViewSets)

urlpatterns= [
    path(
        "api/books/",
        BookListCreateAPIView.as_view(),
        name="book_list_create_view",
    ),

    path('api/', include(router.urls)),
]