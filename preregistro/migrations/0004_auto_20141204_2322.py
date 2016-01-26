# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preregistro', '0003_auto_20141204_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='temario',
            field=models.FileField(null=True, upload_to=b''),
        ),
    ]
