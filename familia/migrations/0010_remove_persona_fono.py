# Generated by Django 4.0.4 on 2022-05-20 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('familia', '0009_persona_fono'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='fono',
        ),
    ]
