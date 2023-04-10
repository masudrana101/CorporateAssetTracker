import django_filters
from django_filters.rest_framework import FilterSet
from .models import Company, Employee, Device, DeviceLog

class CompanyFilter(FilterSet):
    class Meta:
        model = Company
        fields = ['id', 'name']

class EmployeeFilter(FilterSet):
    class Meta:
        model = Employee
        fields = ['id', 'company']

class DeviceFilter(FilterSet):
    class Meta:
        model = Device
        fields = ['id', 'name', 'company', 'model', 'brand', 'serial_number']

class DeviceLogFilter(FilterSet):
    class Meta:
        model = DeviceLog
        fields = ['id', 'device', 'employee', 'checkout_date', 'checkin_date']