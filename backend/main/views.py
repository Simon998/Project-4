from django.shortcuts import render
#added
from rest_framework.views import APIView
from .serializers import EmployeeSerializer
from . import models
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions #for authentication in api

# Create your views here.
class EmployeeList(generics.ListCreateAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]