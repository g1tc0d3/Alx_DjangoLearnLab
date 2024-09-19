from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer

# Create your views here.

class PostListCreateApiView(generics.ListCreateAPIView):
    authentication_classes = TokenAuthentication
    permission_classes = IsAuthenticated
    queryset = Post.objects.all()
    serializer = PostSerializer


