# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodie', '0002_auto_20150927_1957'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='eventfinish',
            new_name='finish',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='eventschool',
            new_name='school',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='eventstart',
            new_name='start',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='eventname',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='goodie',
            old_name='goodiematric',
            new_name='matric',
        ),
        migrations.RenameField(
            model_name='goodie',
            old_name='goodietime',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='school',
            old_name='schoolcode',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='school',
            old_name='schoolname',
            new_name='name',
        ),
    ]
