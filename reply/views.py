from user.permissions import IsOwnerOrReadOnly
from .serializers import ReplySerializer
from .models import Reply
from rest_framework import permissions
from user_profile.permissions import IsOwnerOrReadOnly
from rest_framework import status, viewsets
from . serializers import ReplySerializer


# Create your views here.
class ReplyViewSet(viewsets.ModelViewSet):
    """Comments"""
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)