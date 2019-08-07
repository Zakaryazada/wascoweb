# Generated by Django 2.1.7 on 2019-03-16 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wasco_app', '0008_auto_20190316_1222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devicedata',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='devicedata',
            name='longitude',
        ),
        migrations.AlterField(
            model_name='devicesettings',
            name='imei_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wasco_app.DeviceData'),
        ),
    ]
