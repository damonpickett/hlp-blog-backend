from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models.blog_post import BlogPost

# Register your models here.
class BlogPostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(BlogPost, BlogPostAdmin)
