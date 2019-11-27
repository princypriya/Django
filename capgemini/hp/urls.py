from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [   
   path('',views.regn),
   path('addnewrec',views.addnewrec),

]
