# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preregistro', '0008_auto_20141207_0018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumno',
            old_name='apellidoMaterno',
            new_name='apellido_materno',
        ),
        migrations.RenameField(
            model_name='alumno',
            old_name='apellidoPaterno',
            new_name='apellido_paterno',
        ),
        migrations.RenameField(
            model_name='alumno',
            old_name='correoElectronico',
            new_name='correo_electronico',
        ),
    ]
