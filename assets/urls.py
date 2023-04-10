from django.urls import path
from .views import CompanyViewSet, EmployeeViewSet, DeviceViewSet, DeviceLogViewSet


urlpatterns = [
    path('company/', CompanyViewSet.as_view({'get': 'list', 'post': 'create'}), name='company'),
    path('company/<int:pk>/', CompanyViewSet.as_view({'get': 'retrieve', 'patch': 'update', 'delete': 'destroy'}), name='company'),
    
    path('employee/', EmployeeViewSet.as_view({'get': 'list', 'post': 'create'}), name='employee'),
    path('employee/<int:pk>/', EmployeeViewSet.as_view({'get': 'retrieve', 'patch': 'update', 'delete': 'destroy'}), name='employee'),

    path('device/', DeviceViewSet.as_view({'get': 'list', 'post': 'create'}), name='device'),
    path('device/<int:pk>/', DeviceViewSet.as_view({'get': 'retrieve', 'patch': 'update', 'delete': 'destroy'}), name='device'),

    path('checkout/', DeviceLogViewSet.as_view({'post': 'checkout'}), name='checkout'),
    path('checkin/<int:pk>/', DeviceLogViewSet.as_view({'patch': 'checkin'}), name='checkin'),
    path('device_log/', DeviceLogViewSet.as_view({'get': 'list'}), name='log'),
    path('device_log/<int:pk>/', DeviceLogViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}), name='log'),

]
