from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField, ModelSerializer
from . models import Reply
from comment.models import Comment

class ReplySerializer(ModelSerializer):
    replied_by = serializers.ReadOnlyField(source='owner.first_name')
    class Meta:
        model =Reply
        fields = ('id','replied_by','comment', 'content')