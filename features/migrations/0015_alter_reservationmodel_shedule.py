# Generated by Django 4.0.4 on 2024-09-23 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0014_remove_schedulemodel_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationmodel',
            name='shedule',
            field=models.TextField(null=True),
        ),
    ]
