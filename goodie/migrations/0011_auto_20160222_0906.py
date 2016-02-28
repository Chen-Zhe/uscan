# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goodie', '0010_event_regex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='regex',
            field=models.TextField(default='(.*)'),
        ),
    ]
