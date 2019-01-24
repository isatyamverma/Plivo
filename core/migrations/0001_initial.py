# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-24 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(editable=False)),
                ('last_updated_at', models.DateTimeField(editable=False)),
                ('email', models.CharField(max_length=127, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(editable=False)),
                ('last_updated_at', models.DateTimeField(editable=False)),
                ('first_name', models.CharField(max_length=127)),
                ('last_name', models.CharField(blank=True, max_length=127, null=True)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddIndex(
            model_name='userprofile',
            index=models.Index(fields=['first_name', 'last_name'], name='core_userpr_first_n_490405_idx'),
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['email'], name='core_user_email_38052c_idx'),
        ),
    ]
