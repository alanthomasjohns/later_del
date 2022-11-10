from email.headerregistry import Group
from rest_framework.routers import DefaultRouter
# from group.views import group_memberViewSet, groupViewSet
from user.views import *
from user_profile.views import ProfileViewSet
from votes.views import VoteViewSet
from comment.views import CommentViewSet
from reply.views import ReplyViewSet
from friends.views import FollowViewSet
from posts.views import PostViewSet
from django.urls import path



from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]


router = DefaultRouter()
# router.register(r'users',UserViewSet,basename='users')
router.register(r'profiles',ProfileViewSet)
router.register(r'posts',PostViewSet)
router.register(r'comments',CommentViewSet)
router.register(r'reply',ReplyViewSet)
router.register(r'votes',VoteViewSet)
# router.register(r'user_register',UserRegisterViewSet,basename='user_register')
router.register(r'follow',FollowViewSet,basename='follow')
# router.register(r'group',groupViewSet,basename='group')
# router.register(r'add_to_group',group_memberViewSet,basename='add_to_group')
urlpatterns+= router.urls