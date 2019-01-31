# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-31 06:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auth'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('movieName', models.CharField(max_length=40)),
                ('movieId', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='RecommendData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('searchedMovieName', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='auth',
            name='password',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='auth',
            name='user',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=40),
        ),
    ]