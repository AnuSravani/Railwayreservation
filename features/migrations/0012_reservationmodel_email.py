# Generated by Django 5.0.3 on 2024-09-23 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0011_alter_reservationmodel_reservastion_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservationmodel',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]