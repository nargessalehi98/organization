# Generated by Django 3.2.9 on 2021-11-23 12:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sysmanagement', '0004_auto_20211123_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='username',
            field=models.CharField(default='d', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='creation_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 23, 12, 35, 59, 996989)),
        ),
        migrations.AlterField(
            model_name='task',
            name='dead_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 3, 12, 35, 59, 997015)),
        ),
    ]
