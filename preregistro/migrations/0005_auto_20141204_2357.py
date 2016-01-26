# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preregistro', '0004_auto_20141204_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='descripcion',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='preRequisitos',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='temario',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
    ]
