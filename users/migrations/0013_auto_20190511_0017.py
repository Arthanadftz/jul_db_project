# Generated by Django 2.2.1 on 2019-05-10 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='full_name',
            field=models.CharField(max_length=255, null=True, verbose_name='Фамилия'),
        ),
    ]
