# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-13 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RentRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_books', models.CharField(max_length=50)),
                ('username', models.CharField(default='{{ request.user }}', max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('book_id', models.CharField(max_length=30)),
            ],
        ),
    ]
