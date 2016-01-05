# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodie', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='eventid',
        ),
        migrations.RemoveField(
            model_name='goodie',
            name='goodieid',
        ),
        migrations.RemoveField(
            model_name='school',
            name='schoolid',
        ),
    ]
