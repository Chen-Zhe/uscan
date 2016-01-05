# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodie', '0007_problem'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='code',
            field=models.CharField(default='asdf', max_length=200),
            preserve_default=False,
        ),
    ]
