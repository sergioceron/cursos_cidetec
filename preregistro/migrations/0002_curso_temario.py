# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('preregistro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='temario',
            field=models.FileField(default=datetime.date(2014, 12, 4), upload_to=b'temarios/'),
            preserve_default=False,
        ),
    ]
