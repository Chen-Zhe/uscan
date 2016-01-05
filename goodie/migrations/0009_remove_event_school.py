# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodie', '0008_event_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='school',
        ),
    ]
