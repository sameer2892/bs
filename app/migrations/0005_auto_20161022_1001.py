# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-22 10:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_project_employee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='cost',
            new_name='estimated_cost',
        ),
    ]
