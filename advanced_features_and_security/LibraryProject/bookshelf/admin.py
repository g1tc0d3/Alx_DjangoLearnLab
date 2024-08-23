from django.contrib import admin
from .models import Books
from .models import CustomUser, CustomUserManager, CustomUserAdmin 

"list_filter", "author", "publication_year"

# Register your models here.
"register," 'admin.ModelAdmin'
"search_fields", "title"
admin.site.register(CustomUser, CustomUserAdmin, CustomUserManager)