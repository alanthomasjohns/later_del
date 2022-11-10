

from django.db import models

from user.models import Account

#create your views here

class Post(models.Model):
    
    owner = models.ForeignKey(Account,related_name='posts',on_delete=models.CASCADE)
    content = models.CharField(max_length=4000)
    slug = models.SlugField(unique=True, null=True)
    post_image = models.ImageField(upload_to="post_image",null=True,blank=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=3000,default=None,blank=True,null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)
    
    
    def __str__(self) :
        return self.content