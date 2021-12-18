from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..serializers.blog_post import BlogPostSerializer
from ..models.blog_post import BlogPost
from django.views import View
import json

class BlogPostsView(APIView):
    # POST a blog entry
    def post(self, request):
        blog_post = BlogPostSerializer(data=request.data)
        if blog_post.is_valid():
            blog_post.save()
            return Response(blog_post.data, status=status.HTTP_201_CREATED)
        else:
            return Response(blog_post.errors, status=status.HTTP_400_BAD_REQUEST)

    # GET all blog entries    
    def get(self, request):
        blog_post = BlogPost.objects.all()
        data = BlogPostSerializer(blog_post, many=True).data
        return Response(data)

class BlogPostView(APIView):
    # PATCH blog post by id
    def patch(self, request, pk):
        blog_post = get_object_or_404(BlogPost, pk=pk)
        updated_blog_post = BlogPostSerializer(blog_post, data=request.data, partial=True)
        if updated_blog_post.is_valid():
            updated_blog_post.save()
            return Response(updated_blog_post.data)
    
    # DELETE
    def delete(self, request, pk):
        blog_post = get_object_or_404(BlogPost, pk=pk)
        blog_post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # GET by id
    def get(self, request, pk):
        blog_post = get_object_or_404(BlogPost, pk=pk)
        data = BlogPostSerializer(blog_post).data
        return Response(data)
