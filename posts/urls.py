from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.posts, name= 'posts'),
    path('<int:pk>/', views.posting, name= 'posting'),
    path('newpost/', views.newpost, name= 'newpost'),
    ] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
