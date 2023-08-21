from django.contrib import admin
from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'timestamp')  # Display these fields in the list view
    search_fields = ('title', 'author')  # Add search fields for title and author

admin.site.register(BlogPost, BlogPostAdmin)
