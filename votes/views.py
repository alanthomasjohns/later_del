from django.shortcuts import render
from rest_framework import viewsets,status,permissions,serializers
from django.shortcuts import get_object_or_404, render
from posts.models import Post

from .permissions import hasSelfVotedOrReadOnly
from .models import Vote
from .serializers import VoteSerializer


# Create your views here.
class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes=[permissions.IsAuthenticated,hasSelfVotedOrReadOnly]
    def perform_create(self, serializer):
        post_instance = get_object_or_404(Post,pk=self.request.data['post'])
        #if user likes the post
        if self.request.data['up_vote']:
            already_up_voted = Vote.objects.filter(post=post_instance,up_vote_by=self.request.user).exists()
            if already_up_voted:
                raise serializers.ValidationError({"message":"You have already like this post"})
            else:
                already_down_voted = Vote.objects.filter(post=post_instance,down_vote_by=self.request.user).first()
                if already_down_voted:
                      already_down_voted.delete()
                serializer.save(up_vote_by=self.request.user,post=post_instance)
        #if dislikes
        else:
              already_down_voted = Vote.objects.filter(post=post_instance,down_vote_by=self.request.user).exists()
              if already_down_voted:
                raise serializers.ValidationError({"message":"You have already dislike this post"})
              else:
                  already_up_voted = Vote.objects.filter(post=post_instance,up_vote_by=self.request.user).first()
                  if already_up_voted:
                        already_up_voted.delete()
                  serializer.save(down_vote_by=self.request.user,post=post_instance)
