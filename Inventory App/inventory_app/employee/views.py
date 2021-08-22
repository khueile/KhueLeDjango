
from employee.models import Employee
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, status, mixins, generics, permissions
from employee.serializers import EmployeeSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from employee.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):#
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)

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
    model=Employee
    serializer_class = EmployeeSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [IsAuthenticated,]
    def perform_create(self,serializer):
        serializer.save(createdby = self.request.user)




class GetEmployee(RetrieveUpdateDestroyAPIView): # Edit PUT, DELETE,
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    permission_classes = [IsAuthenticated, ]


