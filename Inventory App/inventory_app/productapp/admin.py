from django.contrib import admin

# Register your models here.
from productapp.models import product
from employee.models import Employee

admin.site.register(product)
admin.site.register(Employee)