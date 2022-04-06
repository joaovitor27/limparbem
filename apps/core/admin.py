
from django.contrib import admin

from .models import Services, Office, Employees, Attendance
# Register your models here.
class AdminServices(admin.ModelAdmin):
    list_display = [
        'name', 'value'
    ]

class AdminOffice(admin.ModelAdmin):
    list_display = [
        'office'
    ]

class AdminEmployees(admin.ModelAdmin):
    list_display = [
        'users'
    ]

class AdminAttendance(admin.ModelAdmin):
    list_display = [
        'services', 'users', 'discount', 'total_value', 'date_attendance', 'date_service', 'status_attendance', 'client_name', 'client_phone', 'client_address'
    ]

admin.site.register(Services, AdminServices)
admin.site.register(Office, AdminOffice)
admin.site.register(Employees, AdminEmployees)
admin.site.register(Attendance, AdminAttendance)