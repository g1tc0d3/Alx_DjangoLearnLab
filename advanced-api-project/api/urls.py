from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomBookListView, CustomBookDetailView, CustomBookCreateView, CustomBookUpdateView, CustomBookDeleteView

router = DefaultRouter()
router.register (r'Books', CustomBookListView)
router.register (r'Books', CustomBookDetailView)
router.register (r'Books/create', CustomBookCreateView)
router.register (r'Books/update', CustomBookUpdateView)
router.register (r'Books/delete', CustomBookDeleteView)

urlpatterns = {
    path('api/', include(router.urls)),
}