from django.urls import path
from .views import *

urlpatterns = [
    path('find/', find_friends.as_view()),
    path('requests/', incoming_requests.as_view()),
    path('followers/', followersAPIView.as_view()),
    path('close_ones/', close_friends.as_view()),
    path('users_list/', users_list.as_view()),
    path('accept/<int:pk>/', AcceptRequestAPI.as_view()),
    # path('delete/' ,undo_request.as_view),
]
