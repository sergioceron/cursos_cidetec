# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preregistro', '0012_auto_20150303_0003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='costo',
            new_name='costo_alumno_ipn',
        ),
        migrations.AddField(
            model_name='curso',
            name='costo_empleado_ipn',
            field=models.DecimalField(null=True, max_digits=9, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='curso',
            name='costo_publico_general',
            field=models.DecimalField(null=True, max_digits=9, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
