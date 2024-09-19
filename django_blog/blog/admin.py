from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Post
# Register your models here.


class CustomUserAdmin (UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets
    pass