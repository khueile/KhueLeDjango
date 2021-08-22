from django.urls import path, include
from employee.views import employee, GetEmployees,GetEmployee
from rest_framework import routers
from employee import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'employee', views.GetEmployees)

app_name='employee'
urlpatterns=[
    #path('', include(router.urls)),
    path('',GetEmployees.as_view(), name='GetEmployees'),
    path('employee/',employee, name='employee'),
    path('<int:pk>/', GetEmployee.as_view(), name='GetEmployee'),

    # URLs for JWT Authentication
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # timelimit #
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  #
]