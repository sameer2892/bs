from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True


class Role(BaseModel):
    name = models.CharField(max_length=200)
    salary = models.FloatField()
    avg_weekly_hours = models.FloatField()

    def __unicode__(self):
        return self.name


class EmployeeStatus(BaseModel):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Employee(BaseModel):
    user = models.OneToOneField(User)
    role = models.ForeignKey(Role)
    employee_status = models.ForeignKey(EmployeeStatus)

    pan = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    address = models.TextField()
    age = models.IntegerField()
    salary = models.FloatField()

    def __unicode__(self):
        return self.user.username


class Client(BaseModel):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class ProjectStatus(BaseModel):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Project(BaseModel):
    status = models.ForeignKey(ProjectStatus)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    start_date = models.DateField()
    finish_date = models.DateField()
    cost = models.FloatField(default=0, editable=False)

    def __unicode__(self):
        return self.name


class Resources(BaseModel):
    project = models.ForeignKey(Project)
    role = models.ForeignKey(Role)
    qty = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.project.name + " - " + self.role.name

    def save(self, *args, **kwargs):
        salary = Role.objects.get(pk=self.role.id).salary * self.qty
        print "salary: ", salary
        months = ((self.project.finish_date - self.project.start_date).days + 1) / 31.0
        print "months: ", months
        cost = float(months * salary)
        print cost
        self.project.cost += cost

        super(Resources, self).save(*args, **kwargs)
        self.project.save()


class TaskStatus(BaseModel):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Task(BaseModel):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    finish_date = models.DateField()
    status = models.ForeignKey(TaskStatus)

    def __unicode__(self):
        return self.name


class TaskAllocation(BaseModel):
    task = models.ForeignKey(Task)
    employee = models.ForeignKey(Employee)

    def __unicode__(self):
        return self.task.name + " - " + self.employee.user.username
