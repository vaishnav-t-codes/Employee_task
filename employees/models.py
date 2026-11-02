from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    phone=models.IntegerField(null=True,unique=True)


class Employee(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    department=models.CharField(max_length=50)
    designation=models.CharField(max_length=100)
    joining_date=models.DateField(auto_now_add=True)


class Task(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=400)
    assigned_to=models.ForeignKey(Employee,on_delete=models.CASCADE,related_name="task")

    PRIORITY_TYPES=(
        ('1',"Low"),
        ('2',"Medium"),
        ('3',"High")
    )

    priority=models.CharField(max_length=100,choices=PRIORITY_TYPES,default="2")

    STATUS=(
        ("pending","Pending"),
        ("in progress","In progress"),
        ("completed","Completed")
    )

    due_date=models.DateField()