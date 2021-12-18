from django.urls import path
from .views import blog_posts

urlpatterns = [
    path('blog_posts/', blog_posts.BlogPostsView.as_view(), name='index'),
    path('blog_posts/<int:pk>/', blog_posts.BlogPostView.as_view(), name='show_blog_post')
]