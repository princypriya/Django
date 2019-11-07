
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('gohome/', views.home),
    path('newuser/',views.newuser_home),
    
]