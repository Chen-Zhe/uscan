# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodie', '0004_goodie_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodie',
            name='event',
            field=models.ForeignKey(to='goodie.Event'),
        ),
    ]
