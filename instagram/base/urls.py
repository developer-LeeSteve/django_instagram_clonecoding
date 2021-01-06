from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from accounts import views as accounts_views
from posts import views as posts_views
from base import views as base_views

urlpatterns = [
	# base
	path('admin/', admin.site.urls),

    # apps
    path('accounts/', include('accounts.urls')),

    path('', base_views.index, name='index'),
    path('create/', posts_views.post_create, name="post_create"),
    path('<str:username>/', base_views.profile, name="base_profile"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)