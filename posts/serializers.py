from rest_framework import serializers
from reply.serializers import ReplySerializer
from comment.serializers import CommentSerializer
from votes.serializers import VoteSerializer
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True,read_only=True)
    reply = ReplySerializer(many=True,read_only=True)
    votes = VoteSerializer(many=True,read_only =True)
    
    class Meta:
        model = Post
        fields = ('id','content','post_image','category','post_date','comments','reply','votes')
        depth=1
            