from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('user.urls')),
    path('api/',include('api.urls')),
    path('api-auth/',include('rest_framework.urls')),
    path('chat/', include('chat.urls')),
    path('comment/', include('comment.urls')),
    path('conversations/', include('chat.urls')),
    path('friends/', include('friends.urls')),
]




urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)