# Generated by Django 3.2.9 on 2021-11-23 12:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sysmanagement', '0003_auto_20211123_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='creation_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 23, 12, 20, 29, 656847)),
        ),
        migrations.AlterField(
            model_name='task',
            name='dead_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 3, 12, 20, 29, 656874)),
        ),
    ]