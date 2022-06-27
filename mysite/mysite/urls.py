from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('about', include('main.urls')),
    path('contacts', include('main.urls')),
    path('new_shoes', include('main.urls')),
    path('most_popular', include('main.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
