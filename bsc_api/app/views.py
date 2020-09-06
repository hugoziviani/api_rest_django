
from rest_framework import viewsets
from app.models import Company, Employee
from app.serealizers import CompanySerealizer, EmployeeSerealizer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerealizer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerealizer

    
