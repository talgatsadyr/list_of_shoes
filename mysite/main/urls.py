from django.urls import path
from .views import index, about, contacts, new_shoes, most_popular
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('contacts', contacts, name='contacts'),
    path('new_shoes', new_shoes, name='new_shoes'),
    path('most_popular', most_popular, name='most_popular'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
