from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomBookListView, CustomBookDetailView, CustomBookCreateView, CustomBookUpdateView, CustomBookDeleteView

router = DefaultRouter()
router.register (r'books', CustomBookListView)
router.register (r'books', CustomBookDetailView)
router.register (r'books/create', CustomBookCreateView)
router.register (r'books/update', CustomBookUpdateView)
router.register (r'books/delete', CustomBookDeleteView)

urlpatterns = {
    path('api/', include(router.urls)),
}