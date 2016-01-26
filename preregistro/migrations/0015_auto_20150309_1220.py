# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preregistro', '0014_alumno_alumnos_inscritos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumno',
            old_name='alumnos_inscritos',
            new_name='cursos_inscritos',
        ),
    ]
