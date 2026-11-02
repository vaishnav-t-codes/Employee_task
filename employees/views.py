from django.shortcuts import render
from employees.models import *
from employees.serializers import *
from rest_framework.generics import CreateAPIView,ListAPIView,DestroyAPIView,RetrieveAPIView,UpdateAPIView
from rest_framework import serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class CreateUser(CreateAPIView):
    serializer_class=UserSerializer

class CreateEmployee(CreateAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all()



class UpdateEmployee(UpdateAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all()

class Destroy(DestroyAPIView):
    serializer_class=EmployeeSerializer
    authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    queryset=Employee.objects.all().delete()

class GetEmployee(ListAPIView):
    serializer_class=EmployeeSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=Employee.objects.all()

class CreateTask(CreateAPIView):
    serializer_class=TaskSerializer
    authentication_classes=[TokenAuthentication]
    authentication_classes=[IsAuthenticated]
    queryset=Task.objects.all()

class RetrieveTask(ListAPIView):
    serializer_class=TaskSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=Task.objects.all()