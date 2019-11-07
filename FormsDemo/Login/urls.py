from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('Login/', views.showscreen),
    path('todo/', views.todofn),
    path('todo/additem', views.additem),
    path('deleteitem/<int:todo_id>', views.deleteitem),
]