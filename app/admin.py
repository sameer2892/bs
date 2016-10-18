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


class ResourcesAdmin(admin.ModelAdmin):
    # list_display = ['project','role']
    # list_editable = ['role']

    class Meta:
        model = Resources


class ProjectAdmin(admin.ModelAdmin):
    class Meta:
        model = Project

    readonly_fields = ('cost',)


class ClientAdmin(admin.ModelAdmin):
    class Meta:
        model = Client


class TaskStatusAdmin(admin.ModelAdmin):
    class Meta:
        model = TaskStatus


class TaskAdmin(admin.ModelAdmin):
    class Meta:
        model = Task


class TaskAllocationAdmin(admin.ModelAdmin):
    class Meta:
        model = TaskAllocation

admin.site.register(Role, RoleAdmin)
admin.site.register(EmployeeStatus, EmployeeStatusAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(ProjectStatus, ProjectStatusAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Resources, ResourcesAdmin)
admin.site.register(TaskStatus, TaskStatusAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(TaskAllocation, TaskAllocationAdmin)
