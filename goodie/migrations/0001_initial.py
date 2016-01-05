# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('eventid', models.IntegerField()),
                ('eventname', models.CharField(max_length=200)),
                ('eventschool', models.IntegerField()),
                ('eventstart', models.DateTimeField()),
                ('eventfinish', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Goodie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('goodieid', models.IntegerField()),
                ('goodiematric', models.CharField(max_length=200)),
                ('goodietime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('schoolid', models.IntegerField()),
                ('schoolname', models.CharField(max_length=200)),
                ('schoolcode', models.IntegerField()),
            ],
        ),
    ]
