# Generated by Django 2.1.7 on 2019-03-07 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wasco_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(max_length=255, unique=True)),
                ('imei_code', models.CharField(max_length=255)),
                ('battery', models.FloatField(blank=True, null=True)),
                ('bin_state', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Device',
                'verbose_name_plural': 'Devices',
            },
        ),
        migrations.CreateModel(
            name='DeviceLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(max_length=255, unique=True)),
                ('imei_code', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Device location',
                'verbose_name_plural': "Devices' locations",
            },
        ),
        migrations.DeleteModel(
            name='Device',
        ),
    ]
