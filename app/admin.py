from django.contrib import admin
from .models import *

# Register your models here.


class RoleAdmin(admin.ModelAdmin):
    class Meta:
        model = Role


class EmployeeStatusAdmin(admin.ModelAdmin):
    class Meta:
        model = EmployeeStatus


class EmployeeAdmin(admin.ModelAdmin):
    class Meta:
        model = Employee

admin.site.register(Role, RoleAdmin)
admin.site.register(EmployeeStatus, EmployeeStatusAdmin)
admin.site.register(Employee, EmployeeAdmin)

