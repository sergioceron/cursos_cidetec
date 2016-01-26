# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preregistro', '0009_auto_20141207_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='alumnos_inscritos',
            field=models.ManyToManyField(to=b'preregistro.Alumno', null=True, blank=True),
        ),
    ]
