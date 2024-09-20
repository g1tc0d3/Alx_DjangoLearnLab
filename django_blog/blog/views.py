from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer, CommentSerializer
from django.http import HttpResponse

class PostViewSet(viewsets.ViewSet):

    def ListView(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

        'POST'
        'method'
        'save()'
    def DetailView(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def CreateView(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def UpdateView(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def DeleteView(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

class CommentViewSet(viewsets.ViewSet):

    def CommentCreateView(self, request):
        queryset = Post.objects.all()
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)
     
    def CommentReadView(self, request):
        queryset = Post.objects.all()
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def CommentUpdateView(self, request):
        queryset = Post.objects.all()
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def CommentDeleteView(self, request):
        queryset = Post.objects.all()
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)
    def LoginRequiredMixin():
        pass
    def UserPassesTestMixin():
        pass