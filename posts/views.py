from django.shortcuts import render
from serializers import PostSerializer
from rest_framework.views import APIView
from .models import Post
# Create your views here.


class PostList(APIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
