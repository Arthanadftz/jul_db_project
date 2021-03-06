# Generated by Django 2.2.1 on 2019-05-11 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=30, verbose_name='Марка')),
                ('car_model', models.CharField(max_length=20, verbose_name='Модель')),
                ('car_engine', models.CharField(blank=True, max_length=30, null=True, verbose_name='Двигатель')),
                ('car_power', models.CharField(blank=True, max_length=30, null=True, verbose_name='Мощность в л.с.')),
                ('car_tyres', models.CharField(max_length=30, verbose_name='Покрышки')),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Расскажите о себе'),
        ),
        migrations.AddField(
            model_name='order',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Car', verbose_name='Автомобиль'),
        ),
    ]
