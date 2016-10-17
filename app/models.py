from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True


class Role(BaseModel):
    name = models.CharField(max_length=200)
    salary = models.FloatField(null=True, blank=True)
    avg_weekly_hours = models.FloatField(null=True, blank=True)

    def __unicode__(self):
        return self.name


class EmployeeStatus(BaseModel):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Employee(BaseModel):
    user = models.OneToOneField(User)
    role = models.ForeignKey(Role, null=True, blank=True)
    employee_status = models.ForeignKey(EmployeeStatus, null=True, blank=True)

    emp_id = models.CharField(max_length=100, null=True, blank=True)
    pan = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    salary = models.FloatField(null=True, blank=True)

    def __unicode__(self):
        return self.user.username
