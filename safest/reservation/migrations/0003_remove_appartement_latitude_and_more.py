# Generated by Django 4.0.4 on 2022-04-19 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_appartement_latitude_appartement_longitude'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appartement',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='appartement',
            name='longitude',
        ),
        migrations.AddField(
            model_name='universite',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='universite',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
    ]
