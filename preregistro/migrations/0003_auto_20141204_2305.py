# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preregistro', '0002_curso_temario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='temario',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
    ]
