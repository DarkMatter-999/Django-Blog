
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from posts.views import index, blog, post, search, contact, works, privacy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', index,name='index'),
    path('blog/', blog, name='blog'),
    path('contact/',contact, name='contact'),
    path('search/', search, name='search'),
    path('post/<title>/', post, name='post'),
    path('howitworks/',works, name='works'),
    path('privacy_policy/',privacy, name='privacy'),
]


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)