# Generated by Django 4.0.4 on 2022-05-20 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familia', '0010_remove_persona_fono'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='fono',
            field=models.IntegerField(default=1),
        ),
    ]
