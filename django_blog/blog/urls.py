from views import PostViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path


router = DefaultRouter
router.register( PostViewSet, basename= 'Post',
    
    )
    
urlpatterns = [
    "post/<int:pk>/delete/", 
    "post/<int:pk>/update/", 
    "post/new/"
    'login/',
    'register/',
    'profile/'
    'Post',
    "comment/<int:pk>/update/",
    "post/<int:pk>/comments/new/",
    "comment/<int:pk>/delete/"
]


