from django.contrib import admin
from .models import Employees, Departments,Manager

admin.site.register(Employees)
admin.site.register(Departments)
admin.site.register(Manager)
