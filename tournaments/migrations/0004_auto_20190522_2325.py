# Generated by Django 2.2.1 on 2019-05-22 20:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0003_auto_20190522_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 22, 20, 25, 13, 417340, tzinfo=utc), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
    ]