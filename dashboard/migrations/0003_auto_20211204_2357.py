# Generated by Django 3.2.9 on 2021-12-04 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_devicelog_device'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devicelog',
            name='device',
        ),
        migrations.DeleteModel(
            name='Device',
        ),
        migrations.DeleteModel(
            name='DeviceLog',
        ),
    ]
