# Generated by Django 4.0.4 on 2022-05-20 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familia', '0008_remove_persona_fono'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='fono',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
