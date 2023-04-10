from rest_framework import serializers
from .models import Company, Employee, Device, DeviceLog
from authentications.models import UserAccount as User
from authentications.serializers import UserSerializer

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'address', 'company_license']
        read_only_fields = ['id']
        

class EmployeeSerializer(serializers.ModelSerializer):
    user_details = serializers.SerializerMethodField()
    class Meta:
        model = Employee
        fields = ['id', 'user', 'company', 'address', 'user_details']
        extra_kwargs = {'user': {'write_only': True}}
        read_only_fields = ['id', 'user_details']


    def get_user_details(self, obj):
        user = User.objects.get(id=obj.user.id)
        return UserSerializer(user).data

class DeviceSerializer(serializers.ModelSerializer):
    company_details = serializers.SerializerMethodField()
    class Meta:
        model = Device
        fields = ['id', 'name', 'company', 'model', 'brand', 'serial_number', 'company_details']
        extra_kwargs = {'company': {'write_only': True}}
        read_only_fields = ['id', 'company_details']

    def get_company_details(self, obj):
        return CompanySerializer(obj.company).data


class DeviceLogSerializer(serializers.ModelSerializer):
    device_details = serializers.SerializerMethodField()
    employee_details = serializers.SerializerMethodField()
    class Meta:
        model = DeviceLog
        fields = ['id', 'device', 'employee', 'checkout_date', 'checkout_condition', 'checkin_date', 'checkin_condition', 'device_details', 'employee_details']
        extra_kwargs = {'device': {'write_only': True}, 'employee': {'write_only': True}}
        read_only_fields = ['id', 'device_details', 'employee_details', 'checkout_date', 'checkin_date']

    def get_device_details(self, obj):
        return DeviceSerializer(obj.device).data

    def get_employee_details(self, obj):
        return EmployeeSerializer(obj.employee).data

class DeviceCheckoutSerializer(serializers.ModelSerializer):
    device_details = serializers.SerializerMethodField()
    employee_details = serializers.SerializerMethodField()
    class Meta:
        model = DeviceLog
        fields = ['id', 'device', 'employee', 'checkout_date', 'checkout_condition', 'device_details', 'employee_details']
        extra_kwargs = {'device': {'write_only': True}, 'employee': {'write_only': True}}
        read_only_fields = ['id', 'device_details', 'employee_details', 'checkout_date']

    def get_device_details(self, obj):
        return DeviceSerializer(obj.device).data

    def get_employee_details(self, obj):
        return EmployeeSerializer(obj.employee).data

class DeviceCheckinSerializer(serializers.ModelSerializer):
    device_details = serializers.SerializerMethodField()
    employee_details = serializers.SerializerMethodField()
    class Meta:
        model = DeviceLog
        fields = ['id', 'device', 'employee', 'checkout_date', 'checkout_condition', 'checkin_date', 'checkin_condition', 'device_details', 'employee_details']
        read_only_fields = ['id', 'device', 'employee', 'checkout_date', 'checkout_condition', 'device_details', 'employee_details']

    def get_device_details(self, obj):
        return DeviceSerializer(obj.device).data

    def get_employee_details(self, obj):
        return EmployeeSerializer(obj.employee).data
    
