from django.contrib.auth.forms import UserCreationForm
from django import forms
from models import CustomUser, Post, Comment

class CommentForm(forms.ModelForm):
    model = Comment
    queryset = 'content'
    