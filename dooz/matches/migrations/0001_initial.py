# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 15:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matchTime', models.DateTimeField()),
                ('has_ended', models.BooleanField(default=False)),
                ('history', models.CommaSeparatedIntegerField(blank=True, default=[], max_length=16)),
                ('blackPlayer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='black_match', to=settings.AUTH_USER_MODEL)),
                ('redPlayer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='red_match', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
