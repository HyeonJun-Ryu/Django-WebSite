from django.urls import path
from . import views

urlpatterns = [
    path('accounts/', views.accounts, name= 'accounts'),
    path('signup/', views.signup, name= 'signup'),
    path('login/', views.login, name= 'login'),
    path('logout/', views.logout, name= 'logout'),
    path('terms/', views.terms, name= 'terms'),
    ]