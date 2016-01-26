# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preregistro', '0013_auto_20150303_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='alumnos_inscritos',
            field=models.ManyToManyField(related_name='cursos', null=True, to='preregistro.Curso', blank=True),
            preserve_default=True,
        ),
    ]
