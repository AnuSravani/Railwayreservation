# Generated by Django 5.0.3 on 2024-09-21 07:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0009_auto_20180318_1412'),
    ]

    operations = [
        migrations.CreateModel(
            name='stationmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_id', models.IntegerField()),
                ('station_name', models.TextField()),
                ('location', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Trainsmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_id', models.IntegerField()),
                ('train_name', models.TextField()),
                ('train_number', models.TextField()),
                ('capacity', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservationmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservastion_id', models.IntegerField()),
                ('shedule', models.TextField()),
                ('reservation_date', models.DateField(auto_now_add=True)),
                ('seat_reserved', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='features.members')),
            ],
        ),
        migrations.CreateModel(
            name='schedulemodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_id', models.IntegerField()),
                ('arrival_time', models.TimeField(auto_now_add=True)),
                ('departure_time', models.TimeField(auto_now_add=True)),
                ('schdule_date', models.DateField(auto_now_add=True)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='features.stationmodel')),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='features.trainsmodel')),
            ],
        ),
    ]