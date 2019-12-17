from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employees
from .serializer import EmployeesSerialiazers
# Create your views here.


class EmpList(APIView):
    def get(self, request):
        e1 = Employees.objects.all()
        serializer  = EmployeesSerialiazers(e1, many=True)
        return Response(serializer.data)
        
    # def post(self):
    #     pass






