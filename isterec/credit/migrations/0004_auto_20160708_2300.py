# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 20:00
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0003_auto_20160708_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditrecdata',
            name='is_selected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='creditrecdata',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='creditrecdata',
            name='rollno',
            field=models.CharField(default='', max_length=15, validators=[django.core.validators.RegexValidator(message='Please enter a valid Roll number.', regex='^(\\d{2}|\\d{8})([a-z]{2}|[A-Z]{2})\\d{2,3}([a-z]{1}|[A-Z]{1})?$')]),
        ),
    ]
