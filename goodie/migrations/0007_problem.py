# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodie', '0006_auto_20150928_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('matric', models.CharField(max_length=200)),
                ('school', models.ManyToManyField(to='goodie.School')),
            ],
        ),
    ]
