from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [   
   path('',views.book),
   path('filtering', views.filtering),
   path('booksrch', views.booksrch),
  
 
  
]

