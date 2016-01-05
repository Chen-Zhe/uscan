# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodie', '0005_auto_20150928_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='school',
        ),
        migrations.AddField(
            model_name='event',
            name='school',
            field=models.ManyToManyField(to='goodie.School'),
        ),
    ]
