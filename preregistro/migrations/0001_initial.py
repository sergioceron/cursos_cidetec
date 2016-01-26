# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=64)),
                ('apellidoPaterno', models.CharField(max_length=64)),
                ('apellidoMaterno', models.CharField(max_length=64)),
                ('tipo', models.CharField(max_length=2, choices=[(b'PG', b'Publico en General'), (b'AP', b'Alumno IPN'), (b'EP', b'Empleado IPN')])),
                ('correoElectronico', models.EmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=64)),
                ('descripcion', models.TextField()),
                ('fechaInicio', models.DateField()),
                ('modalidad', models.CharField(max_length=2, choices=[(b'SE', b'Semanal'), (b'SA', b'Sabatino')])),
                ('preRequisitos', models.TextField()),
                ('numeroHoras', models.SmallIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
