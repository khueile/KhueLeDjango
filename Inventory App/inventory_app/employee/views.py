from employee.models import Employee
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from employee.serializers import EmployeeSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

@api_view(['GET','POST'])
def employee(request):
    if request.method=='GET':
        employees=Employee.objects.all()
        return Response(EmployeeSerializer(employees, many=True).data, status=status.HTTP_200_OK)
    else:
        employees=EmployeeSerializer(request.data)
        if employees.is_valid():
            employees.save()
            return Response(employees.data, status=status.HTTP_201_CREATED)
        else:
            return Response(employees.data, status=status.HTTP_400_BAD_REQUEST)

class GetEmployees(ListCreateAPIView):
    queryset = Employee.objects.all()
    #model=Employee
    serializer_class = EmployeeSerializer

class GetEmployee(RetrieveUpdateDestroyAPIView): # Edit PUT, DELETE,
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer



