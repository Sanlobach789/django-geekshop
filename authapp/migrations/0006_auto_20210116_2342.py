# Generated by Django 2.2.17 on 2021-01-16 20:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_auto_20210116_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 18, 20, 42, 55, 371569, tzinfo=utc)),
        ),
    ]
