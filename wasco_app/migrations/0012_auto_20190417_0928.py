# Generated by Django 2.1.7 on 2019-04-17 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wasco_app', '0011_auto_20190417_0928'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='devicedata',
            options={'ordering': ['order'], 'verbose_name': 'Device data', 'verbose_name_plural': 'Device data'},
        ),
        migrations.AlterModelOptions(
            name='devicesettings',
            options={'ordering': ['order'], 'verbose_name': 'Device location', 'verbose_name_plural': 'Device location'},
        ),
    ]
