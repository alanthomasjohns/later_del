from django.shortcuts import render
from rest_framework import viewsets,status,permissions
from rest_framework.generics import ListAPIView
from .serializers import PostSerializer
from .models import Post
from user_profile.permissions import IsOwnerOrReadOnly

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    # def retreive(self,request, serializer):
    #     post = Post.objects.filter(user = )
        