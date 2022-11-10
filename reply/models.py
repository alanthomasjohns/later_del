from django.db import models
from comment.models import Comment
from posts.models import Post
from user.models import Account
# Create your models here.

class Reply(models.Model):
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, related_name='reply',on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content
