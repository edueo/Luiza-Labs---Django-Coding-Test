"""vagaped URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from rest_framework import routers, serializers, viewsets
from employeemanager.models import Employee, Department

class DepartmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Department
        fields = ('title', ) 

class EmployeeSerializer(serializers.ModelSerializer):
    #department = serializers.StringRelatedField(many=False)
    
    
    department = DepartmentSerializer(many=False)

    class Meta:
        model = Employee
        fields = ('name', 'email', 'department')
    
    def create(self, validated_data):
        department = validated_data.pop('department')
        department = Department.objects.create(title=department['title'])
        
        name = validated_data.pop('name')
        email = validated_data.pop('email')

        employee = Employee.objects.create(name=name, email=email,
                                           department_id=department.id)
        return employee



class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewSet)




urlpatterns = [
    url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls'))
]
