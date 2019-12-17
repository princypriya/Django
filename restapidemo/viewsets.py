from restapidemo.models import Employees
from .serializer import EmployeesSerialiazers
from rest_framework import  viewsets

class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerialiazers
    