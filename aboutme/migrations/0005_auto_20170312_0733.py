# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-12 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutme', '0004_auto_20170312_0705'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usetechnial',
            old_name='usetime',
            new_name='end_time',
        ),
        migrations.AddField(
            model_name='usetechnial',
            name='start_time',
            field=models.DateField(blank=True, null=True),
        ),
    ]