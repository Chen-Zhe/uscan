# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goodie', '0009_remove_event_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='regex',
            field=models.TextField(default='.*'),
            preserve_default=False,
        ),
    ]
