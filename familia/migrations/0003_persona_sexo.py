# Generated by Django 4.0.4 on 2022-05-19 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familia', '0002_persona_fecha_nacimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='sexo',
            field=models.CharField(default='Femenino', max_length=10),
        ),
    ]
