# Generated by Django 2.2.17 on 2021-01-16 20:01

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_auto_20210116_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 18, 20, 1, 48, 814220, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagline', models.CharField(blank=True, max_length=128, verbose_name='теги')),
                ('aboutMe', models.TextField(blank=True, max_length=512, verbose_name='о себе')),
                ('gender', models.CharField(blank=True, choices=[('M', 'М'), ('W', 'Ж')], max_length=1, verbose_name='пол')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
