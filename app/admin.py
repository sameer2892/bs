from django.contrib import admin
from .models import *

# Register your models here.


class RoleAdmin(admin.ModelAdmin):
    class Meta:
        model = Role

    list_display = ['name', 'salary', 'avg_weekly_hours']


class EmployeeStatusAdmin(admin.ModelAdmin):
    class Meta:
        model = EmployeeStatus


class EmployeeAdmin(admin.ModelAdmin):
    class Meta:
        model = Employee

    list_display = ['user', 'role', 'employee_status', 'salary', 'phone', 'pan', 'address', 'age']


class ProjectStatusAdmin(admin.ModelAdmin):
    class Meta:
        model = ProjectStatus


class ResourcesAdmin(admin.ModelAdmin):
    list_display = ['project', 'role', 'qty']
    # list_editable = ['role']

    class Meta:
        model = Resources


class ProjectAdmin(admin.ModelAdmin):
    class Meta:
        model = Project

    readonly_fields = ('estimated_cost', 'signoff_date')
    list_display = ['name', 'client', 'start_date', 'finish_date', 'status', 'estimated_cost', 'signoff', 'final_quote', 'amount_received', 'amount_due']
    list_editable = ['signoff', 'final_quote']


class ClientAdmin(admin.ModelAdmin):
    class Meta:
        model = Client


class TaskStatusAdmin(admin.ModelAdmin):
    class Meta:
        model = TaskStatus


class TaskAdmin(admin.ModelAdmin):
    class Meta:
        model = Task

    list_display = ['name', 'start_date', 'finish_date', 'status']
    list_editable = ['start_date', 'finish_date', 'status']

# class TaskAllocationAdmin(admin.ModelAdmin):
#     class Meta:
#         model = TaskAllocation


class MilestonesAdmin(admin.ModelAdmin):
    class Meta:
        model = Milestones

    list_display = ['name', 'project', 'end_date', 'amount_percentage', 'payment_received']
    list_editable = ['payment_received']


class TransactionsAdmin(admin.ModelAdmin):
    class Meta:
        model = Transactions
    list_display = ['project', 'payment_type', 'payment_received_by', 'amount']

admin.site.register(Transactions, TransactionsAdmin)
admin.site.register(Milestones, MilestonesAdmin)
admin.site.register(PaymentType)
admin.site.register(Role, RoleAdmin)
admin.site.register(EmployeeStatus, EmployeeStatusAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(ProjectStatus, ProjectStatusAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Resources, ResourcesAdmin)
admin.site.register(TaskStatus, TaskStatusAdmin)
admin.site.register(Task, TaskAdmin)
# admin.site.register(TaskAllocation, TaskAllocationAdmin)
