# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preregistro', '0007_curso_almnos_inscritos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='almnos_inscritos',
            new_name='alumnos_inscritos',
        ),
    ]
