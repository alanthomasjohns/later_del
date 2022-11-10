from django.db.models import Q
from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from user.permissions import IsOwnerOrReadOnly
from .serializers import CommentSerializer

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from .models import Comment

from .models import Comment
from rest_framework import permissions
from user_profile.permissions import IsOwnerOrReadOnly
from rest_framework import status, viewsets
from . serializers import CommentSerializer


# Create your views here.
class CommentViewSet(viewsets.ModelViewSet):
    """Comments"""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



# class PostCreateAPIView(CreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = PostCreateUpdateSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)



class CommentDetailAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # lookup_field = 'slug'


# class PostUpdateAPIView(RetrieveUpdateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = PostCreateUpdateSerializer
#     lookup_field - 'slug'
#     permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

#     def perform_update(self, serializer):
#         serializer.save(user = self.request.user)


# class CommentDeleteAPIView(DestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer


class CommentListAPIView(ListAPIView):
    serializer_class = CommentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content', 'user__first_name']


    def get_queryset(self, *args, **kwargs):
        queryset_list = Comment.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(content__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query) 
            ).distinct()
        return queryset_list


