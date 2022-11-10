from django.db import models

from posts.models import Post
from user.models import Account
# Create your models here.
class Comment(models.Model):
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete = models.CASCADE)
    content = models.TextField(null=True)
    comment_image=models.ImageField(upload_to="comment_image",null=True,blank=True)
    comment_date=models.DateField(auto_now_add=True, null=True)
    def __str__(self):
        return self.content




# class Comment(models.Model):
#     owner = models.ForeignKey(Account, on_delete=models.CASCADE)
#     post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
#     parent = models.ForeignKey("self", null=True, blank=True, on_delete = models.CASCADE)
#     content = models.TextField(null=True)
#     comment_image=models.ImageField(upload_to="comment_image",null=True,blank=True)
#     comment_date=models.DateField(auto_now_add=True, null=True)
#     def __str__(self):
#         return self.comment


#     def __str__(self):
#         return str(self.owner.first_name)

#     def children(self):
#         obj = Comment.objects.filter(parent=self)
#         return obj