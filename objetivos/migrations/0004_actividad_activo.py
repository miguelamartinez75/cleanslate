# Generated by Django 4.0.2 on 2022-05-03 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objetivos', '0003_actividad_duracion_actividad_problema_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]
