from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('oops/', views.noacc, name= 'noacc'),
    ]