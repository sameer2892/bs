# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_milestones_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='milestones',
            name='payment_received',
            field=models.BooleanField(default=False, help_text='Check if payment has been received'),
        ),
    ]
