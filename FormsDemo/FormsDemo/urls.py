
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('Login.urls')),
    path('Login/', include('Login.urls')),
    path('admin/', admin.site.urls),
    path('todo/', include('Login.urls')),
    path('todo/additem', include('Login.urls')),
    path('deleteitem/<int:todo_id>', include('Login.urls')),
    path('', include('newuserapp.urls')),
    path('newuser/', include('newuserapp.urls')),
    path('gohome/', include('newuserapp.urls'))

    
]
