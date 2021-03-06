# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-19 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0003_auto_20200318_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentrequest',
            name='books',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='rentrequest',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='rentrequest',
            name='total_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='rentrequest',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
