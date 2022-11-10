from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField, ModelSerializer, SerializerMethodField
from . models import Comment
from reply.serializers import ReplySerializer

class CommentSerializer(serializers.ModelSerializer):
    commented_by = serializers.ReadOnlyField(source='owner.email')
    replies = ReplySerializer(many=True,read_only=True)
    print(f'this is {commented_by}')
    class Meta:
        model =Comment
        fields = ('id','content','parent','comment_image','commented_by','replies', 'content')
        depth=1






# class CommentSerializer(ModelSerializer):
#     commented_by = serializers.ReadOnlyField(source='owner.email')
#     reply_count = SerializerMethodField()
#     replies = SerializerMethodField()
#     class Meta:
#         model =Comment
#         fields = ('id','content','parent','comment_image', 'commented_by', 'content','replies', 'reply_count')


#     def get_reply_count(self, obj):
#         if obj.is_parent:
#             return obj.children().count()
#         return 0

#     def get_replies(self, obj) :
#         if obj.is_parent:
#             return CommentChildSerializer(obj.children(),many=True).data
#         return None


# class CommentChildSerializer(ModelSerializer):
#     class Meta:
#         model =Comment
#         fields = ('id','content', 'timestamp')


# class CommentDetailSerializer(ModelSerializer):
#     replies = SerializerMethodField()
#     class Meta:
#         model =Comment
#         fields = ('id','content', 'replies')

#     def get_replies(self, obj) :
#         if obj.is_parent:
#             return CommentChildSerializer(obj.children(),many=True).data
#         return None
     
     




    