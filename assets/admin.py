from django.contrib import admin
from .models import Company, Employee, Device, DeviceLog
# Register your models here.

admin.site.register([Company, Employee, Device, DeviceLog])

