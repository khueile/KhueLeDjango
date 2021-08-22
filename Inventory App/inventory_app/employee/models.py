from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Employee(models.Model):#ORM established
    First_Name = models.CharField(max_length=55)
    Last_Name = models.CharField(max_length=55)
    Department = models.CharField(max_length=55)
    Salary= models.PositiveIntegerField(default=0)
    date_added = models.DateField(default=datetime.date.today)
    createdby = models.ForeignKey(User, on_delete=models.CASCADE, default =None)# permissions


    def __str__(self):
        return self.First_Name