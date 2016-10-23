# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 09:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_auto_20161023_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='signoff_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]