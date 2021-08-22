
from employee.models import Employee
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
class EmployeeSerializer(ModelSerializer):
    createdby = serializers.ReadOnlyField(source='createdby.username')
    class Meta:
        model=Employee
        fields='__all__'