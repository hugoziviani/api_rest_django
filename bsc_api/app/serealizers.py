from app.models import Employee, Company
from rest_framework import serializers

class CompanySerealizer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            'name',
            'institutional_registry',
            'created_at'
        ]

class EmployeeSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'work_for',
            'joined_at'
        ]
