# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
