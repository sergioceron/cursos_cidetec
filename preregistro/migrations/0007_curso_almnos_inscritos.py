# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preregistro', '0006_auto_20141205_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='almnos_inscritos',
            field=models.ManyToManyField(to='preregistro.Alumno'),
            preserve_default=True,
        ),
    ]
