# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 17:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
                ('volume', models.CharField(max_length=10)),
                ('page', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='texasfile.Resource'),
        ),
    ]