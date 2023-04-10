from django.shortcuts import render
from .models import Company, Employee, Device, DeviceLog
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, DeviceLogSerializer, DeviceCheckoutSerializer, DeviceCheckinSerializer
from .filters import CompanyFilter, EmployeeFilter, DeviceFilter, DeviceLogFilter 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status, viewsets, filters
from rest_framework.permissions import IsAuthenticated
from utils.response_wrapper import ResponseWrapper
from rest_framework.response import Response
from django.db.models import Q


# Create your views here.
# Using filter() instead of get() where needed because get() will throw an exception if no object is found

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAdminUser]
    lookup_field = 'pk'
    filterset_class = CompanyFilter
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filterset_fields = ('id', 'name')

    # This method will be called when a POST request is made to the endpoint, and it will create a new company
    def create(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return ResponseWrapper(
                    data=serializer.data,
                    message='Company created',
                    status=status.HTTP_201_CREATED
                )
            else:
                return ResponseWrapper(
                    message=serializer.errors,
                    error_code=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )

    # This method will be called when a GET request is made to the endpoint, and it will return a list of all companies (Pagination is also implemented by default rest_framework pagination)
    def list(self, request):
        try:
            qs = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(qs, many=True)
            return ResponseWrapper(
                data=serializer.data,
                message='Company list',
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )

    # This method will be called when a GET request is made to the endpoint with a company id, and it will return a single company
    def retrieve(self, request, *args, **kwargs):
        try:
            company = Company.objects.filter(id=kwargs['pk']).first()
            serializer = self.get_serializer(company)
            return ResponseWrapper(
                data=serializer.data,
                message='Company retrieved',
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )

    # This method will be called when a PATCH request is made to the endpoint with a company id, and it will update a single company (Partial update thats why using PATCH)
    def update(self, request, *args, **kwargs):
        try:
            company = Company.objects.filter(id=kwargs['pk']).first()
            serializer = self.get_serializer(company, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return ResponseWrapper(
                    data=serializer.data,
                    message='Company updated',
                    status=status.HTTP_200_OK
                )
            else:
                return ResponseWrapper(
                    message=serializer.errors,
                    error_code=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )

    # This method will be called when a DELETE request is made to the endpoint with a company id, and it will delete a single company
    def destroy(self, request, *args, **kwargs):
        try:
            company = Company.objects.filter(id=kwargs['pk']).first()
            company.delete()
            return ResponseWrapper(
                message='Company deleted',
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'
    filterset_class = EmployeeFilter
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filterset_fields = ('id', 'company')

    # This method will be called when a POST request is made to the endpoint, and it will create a new employee
    def create(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return ResponseWrapper(
                    data=serializer.data,
                    message='Employee created',
                    status=status.HTTP_201_CREATED
                )
            else:
                return ResponseWrapper(
                    message=serializer.errors,
                    error_code=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )

    # This method will be called when a GET request is made to the endpoint, and it will return a list of all employees (Pagination is also implemented by default rest_framework pagination)
    def list(self, request):
        try:
            qs = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(qs, many=True)
            return ResponseWrapper(
                data=serializer.data,
                message='Employee list',
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )

    # This method will be called when a GET request is made to the endpoint with a employee id, and it will return a single employee
    def retrieve(self, request, *args, **kwargs):
        try:
            employee = Employee.objects.filter(id=kwargs['pk']).first()
            serializer = self.get_serializer(employee)
            return ResponseWrapper(
                data=serializer.data,
                message='Employee retrieved',
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )

    # This method will be called when a PATCH request is made to the endpoint with a employee id, and it will update a single employee (Partial update thats why using PATCH)
    def update(self, request, *args, **kwargs):
        try:
            employee = Employee.objects.filter(id=kwargs['pk']).first()
            serializer = self.get_serializer(employee, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return ResponseWrapper(
                    data=serializer.data,
                    message='Employee updated',
                    status=status.HTTP_200_OK
                )
            else:
                return ResponseWrapper(
                    message=serializer.errors,
                    error_code=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )

    # This method will be called when a DELETE request is made to the endpoint with a employee id, and it will delete a single employee
    def destroy(self, request, *args, **kwargs):
        try:
            employee = Employee.objects.filter(id=kwargs['pk']).first()
            employee.delete()
            return ResponseWrapper(
                message='Employee deleted',
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'
    filterset_class = DeviceFilter
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filterset_fields = ('id', 'company', 'employee')

    # def get_permissions(self):
    #     if self.action == 'list' or self.action == 'retrieve':
    #         permission_classes = [permissions.AllowAny]
    #     else:
    #         permission_classes = [permissions.IsAdminUser]
    #     return [permission() for permission in permission_classes]

    # This method will be called when a POST request is made to the endpoint, and it will create a new device
    def create(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return ResponseWrapper(
                    data=serializer.data,
                    message='Device created',
                    status=status.HTTP_201_CREATED
                )
            else:
                return ResponseWrapper(
                    message=serializer.errors,
                    error_code=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )

    # This method will be called when a GET request is made to the endpoint, and it will return a list of all devices (Pagination is also implemented by default rest_framework pagination)
    def list(self, request):
        try:
            qs = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(qs, many=True)
            return ResponseWrapper(
                data=serializer.data,
                message='Device list',
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )

    # This method will be called when a GET request is made to the endpoint with a device id, and it will return a single device
    def retrieve(self, request, *args, **kwargs):
        try:
            device = Device.objects.filter(id=kwargs['pk']).first()
            serializer = self.get_serializer(device)
            return ResponseWrapper(
                data=serializer.data,
                message='Device retrieved',
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )

    # This method will be called when a PATCH request is made to the endpoint with a device id, and it will update a single device (Partial update thats why using PATCH)
    def update(self, request, *args, **kwargs):
        try:
            device = Device.objects.filter(id=kwargs['pk']).first()
            serializer = self.get_serializer(device, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return ResponseWrapper(
                    data=serializer.data,
                    message='Device updated',
                    status=status.HTTP_200_OK
                )
            else:
                return ResponseWrapper(
                    message=serializer.errors,
                    error_code=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )

    # This method will be called when a DELETE request is made to the endpoint with a device id, and it will delete a single device
    def destroy(self, request, *args, **kwargs):
        try:
            device = Device.objects.filter(id=kwargs['pk']).first()
            device.delete()
            return ResponseWrapper(
                message='Device deleted',
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )


class DeviceLogViewSet(viewsets.ModelViewSet):
    queryset = DeviceLog.objects.all()
    #serializer_class = DeviceLogSerializer
    #permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'
    filterset_class = DeviceLogFilter
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filterset_fields = ('id', 'device', 'employee', 'checkout_date', 'checkin_date')

    # this method needed custom permission classes for each action
    def get_permissions(self):
        if self.action == 'destroy':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    # this method needed custom serializer classes for each action
    def get_serializer_class(self):
        if self.action == 'checkout':
            return DeviceCheckoutSerializer
        elif self.action == 'checkin':
            return DeviceCheckinSerializer
        else:
            return DeviceLogSerializer

    # checkout device and create a new device log
    def checkout(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return ResponseWrapper(
                    data=serializer.data,
                    message='Device checked out',
                    status=status.HTTP_201_CREATED
                )
            else:
                return ResponseWrapper(
                    message=serializer.errors,
                    error_code=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )

    # checkin device and update the device log
    def checkin(self, request, *args, **kwargs):
        try:
            device_log = DeviceLog.objects.filter(id=kwargs['pk']).first()
            serializer = self.get_serializer(device_log, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return ResponseWrapper(
                    data=serializer.data,
                    message='Device checked in',
                    status=status.HTTP_200_OK
                )
            else:
                return ResponseWrapper(
                    message=serializer.errors,
                    error_code=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )

    # this method will be called when a GET request is made to the endpoint, and it will return all device logs
    def list(self, request):
        try:
            qs = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(qs, many=True)
            return ResponseWrapper(
                data=serializer.data,
                message='Device log list',
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )

    # this method will be called when a GET request is made to the endpoint with a device log id, and it will return a single device log
    def retrieve(self, request, *args, **kwargs):
        try:
            device_log = DeviceLog.objects.filter(id=kwargs['pk']).first()
            serializer = self.get_serializer(device_log)
            return ResponseWrapper(
                data=serializer.data,
                message='Device log retrieved',
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )

    # this method will be called when a PATCH request is made to the endpoint with a device log id, and it will update a single device log (Partial update thats why using PATCH)
    def destroy(self, request, *args, **kwargs):
        try:
            device_log = DeviceLog.objects.filter(id=kwargs['pk']).first()
            device_log.delete()
            return ResponseWrapper(
                message='Device log deleted',
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )


