# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preregistro', '0010_auto_20141207_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='costo',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
