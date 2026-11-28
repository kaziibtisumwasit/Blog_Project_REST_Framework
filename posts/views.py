from django.shortcuts import render
from . import serializers
from rest_framework.views import APIView
from .models import Post
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import HTTP_404_NOT_FOUND



# Create your views here.


class PostList(APIView):
    # queryset = Post.objects.all()
    # serializer_class = serializers.PostSerializer
    ## format = None // Jekono type er data accept korbe ei view
    def get(self, request, fromat=None): ## view ba only read er request handle korbe ei method
        print("inside get in postlist")
        post = Post.objects.all()
        # serializer wrok on both serialize & Deserialize
        ## many=True means multiple object will be serialized
        serializer = serializers.PostSerializer(post, many=True)
        return Response(serializer.data) ## return data in json format
    
    
    def post(self, request ,format=None):
        print("inside POST method in postlist")
        
        serializer = serializers.PostSerializer(data=request.data) ## user der dewa data nilam
        if serializer.is_valid(): ## check korlam data valid kina
            serializer.save() ## save korlam data
            ## rest_framework give use status we access it status.
            return Response(serializer.data,status.HTTP_201_CREATED) ## return data in json format
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST) ## return error if data is not valid




## get e particular ekta object ke niye ashe.
## filter e list of object ba queryset pabo.

class PostDetail(APIView):
        def get_object(self, pk):
              
            try:
                return Post.objects.get(pk=pk)
            except Post.DoesNotExist:
                raise status.HTTP_404_NOT_FOUND
              
              
              
        def get(self, request, pk, format=None):
            post = self.get_object(pk)
            serializer = serializers.PostSerializer(post)
            return Response(serializer.data)
        
        def put(self, request , pk , format = None):
            post = self.get_object(pk=pk)
            serializer = serializers.PostSerializer(post, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)