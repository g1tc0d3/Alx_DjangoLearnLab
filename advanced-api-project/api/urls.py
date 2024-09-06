from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomBookListView, CustomBookDetailView, CustomBookCreateView, CustomBookUpdateView, CustomBookDeleteView

router = DefaultRouter()
router.register (r'Book', CustomBookListView)
router.register (r'Book', CustomBookDetailView)
router.register (r'Book', CustomBookCreateView)
router.register (r'Book', CustomBookUpdateView)
router.register (r'Book', CustomBookDeleteView)

urlpatterns = {
    path('api/', include(router.urls)),
}