# Generated by Django 3.2.9 on 2021-11-23 12:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sysmanagement', '0002_alter_task_dead_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='creation_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 3, 12, 18, 15, 677666)),
        ),
        migrations.AlterField(
            model_name='task',
            name='dead_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 23, 12, 18, 15, 677698)),
        ),
    ]
