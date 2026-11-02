from rest_framework import serializers
from employees.models import *


class UserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=CustomUser
        fields=["id","username","email","password","phone"]
        read_only_fields=["id",]
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"
        read_only_fields=["id","joining_date"]

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        models=Task
        fields="__all__"
        read_only_fields=["id"]
