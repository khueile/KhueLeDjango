from django.urls import path
from employee.views import employee, GetEmployees,GetEmployee

app_name='employee'
urlpatterns=[
    path('',GetEmployees.as_view(), name='GetEmployees'),
    path('employee/',employee, name='employee'),
    path('<int:pk>/', GetEmployee.as_view(), name='GetEmployee'),

]