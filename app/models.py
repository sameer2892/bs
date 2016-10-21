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

    def save(self, *args, **kwargs):
        start_date_old = Project.objects.get(pk=self.id).start_date
        finish_date_old = Project.objects.get(pk=self.id).finish_date
        resource_obj = Resources.objects.filter(project=self)
        print 5555
        print "old start date: ", start_date_old
        print "old finish date: ", finish_date_old
        print "new start date: ", self.start_date
        print "new finish date: ", self.finish_date
        super(Project, self).save()
        if self.start_date != start_date_old or self.finish_date != finish_date_old:
            print 666666
            self.cost = 0
            print resource_obj
            for each in resource_obj:
                print 77777
                print each.project.name
                cost_temp = each.update_cost()
                print 888888
                print "project cost: ", cost_temp
                self.cost += cost_temp
        super(Project, self).save()


class Resources(BaseModel):
    project = models.ForeignKey(Project)
    role = models.ForeignKey(Role)

    qty = models.IntegerField()

    def __unicode__(self):
        return self.project.name + " - " + self.role.name

    def save(self, *args, **kwargs):
        # role_old = Resources.objects.get(pk=self.id).role
        # qty_old = Resources.objects.get(pk=self.id).qty
        # if self.role != role_old or self.qty != qty_old:
        self.update_cost()
        super(Resources, self).save()
        # super(Resources, self).save()

    def update_cost(self):
        print 11111
        resource_obj = Resources.objects.filter(pk=self.id)
        months = float((self.project.finish_date - self.project.start_date).days + 1.0)
        print "days: ", months
        months = float(months/31)
        if resource_obj:
            print 222222
            for resource in resource_obj:
                print 33333
                salary_old = Role.objects.get(pk=resource.role.id).salary * resource.qty

                cost_old = float(months * salary_old)
                self.project.cost -= cost_old
        print 4444
        salary = Role.objects.get(pk=self.role.id).salary * self.qty
        print "salary: ", salary

        print "months: ", months
        cost = float(months * salary)
        print cost

        self.project.cost += cost
        # super(Project, self.project).save()
        self.project.save()
        print self.project.cost
        print self.project.name
        super(Resources, self).save()
        print "resource cost: ", cost
        return cost


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
