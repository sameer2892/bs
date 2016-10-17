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


class ProjectStatusAdmin(admin.ModelAdmin):
    class Meta:
        model = ProjectStatus


class ProjectAdmin(admin.ModelAdmin):
    class Meta:
        model = Project


class ProjectResourcesAdmin(admin.ModelAdmin):
    class Meta:
        model = ProjectResources


class ClientAdmin(admin.ModelAdmin):
    class Meta:
        model = Client

admin.site.register(Role, RoleAdmin)
admin.site.register(EmployeeStatus, EmployeeStatusAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(ProjectStatus, ProjectStatusAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectResources, ProjectResourcesAdmin)
admin.site.register(Client, ClientAdmin)

