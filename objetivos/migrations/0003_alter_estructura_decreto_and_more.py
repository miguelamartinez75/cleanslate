# Generated by Django 4.0.2 on 2022-03-08 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objetivos', '0002_alter_estructura_decreto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estructura',
            name='decreto',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='estructura',
            name='diagnostico',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='estructura',
            name='function',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='estructura',
            name='letra',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='estructura',
            name='marco_legal',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='estructura',
            name='mission',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='estructura',
            name='procesos_participativos',
            field=models.TextField(null=True),
        ),
    ]