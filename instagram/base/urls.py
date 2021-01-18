from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from posts import views as posts_views

urlpatterns = [
	# base
	path('admin/', admin.site.urls),

    # apps
    path('', include('accounts.urls')),
    path('posts/', include('posts.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)