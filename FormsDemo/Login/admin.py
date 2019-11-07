from django.contrib import admin
from .models import LoginForm
from .models import Todo

admin.site.register(LoginForm)
admin.site.register(Todo)

# Register your models here.
