# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-05-26 16:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('founder', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='SuperHeroe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('gender', models.CharField(blank=True, default='', max_length=100)),
                ('real_name', models.CharField(blank=True, default='', max_length=100)),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='horactual.Publisher')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
