


# from django.urls import re_path as url
# from django.contrib import admin


# from .views import *
# urlpatterns = [
#     url(r'^$', CommentListAPIView.as_view(), name='list'),
#     url(r'^(?P<pk>\d+)/$', CommentDetailAPIView.as_view(), name='delete'),
# ]


from django.urls import re_path as url
from django.contrib import admin


from .views import *
urlpatterns = [
    url(r'^$', CommentListAPIView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', CommentDetailAPIView.as_view(), name='delete'),
]