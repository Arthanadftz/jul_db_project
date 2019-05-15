from django.conf import settings
from django.db import models
from django.urls import reverse
# Create your models here.

class Car(models.Model):
    car_name = models.CharField(max_length=30, verbose_name="Марка")
    car_model = models.CharField(max_length=20, verbose_name="Модель")
    car_engine = models.CharField(max_length=30, verbose_name="Двигатель", default="Нет данных")
    car_power = models.CharField(max_length=30, verbose_name="Мощность в л.с.", default="Нет данных")
    car_tyres = models.CharField(max_length=30, verbose_name="Покрышки", default="Нет данных")

    def __str__(self):
        return f'{self.car_name} {self.car_model}'


class Order(models.Model):
    READY = 'ГТВ'
    WIP = 'ОБР'

    STATUS_CHOICES = (
        (READY, 'Готово'),
        (WIP, 'Обработка')
    )
    status = models.CharField(max_length=3,
        choices=STATUS_CHOICES,
        default=WIP,
        verbose_name='Статус заявки'
    )

    title = models.CharField(max_length=255, verbose_name="Расскажите о себе")
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name = "Заказчик"
    )
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name = "Автомобиль", null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('order_detail', args=[str(self.id)])


class Feedback(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name = "Пользователь"
    )
    title = models.CharField(max_length=255, verbose_name="Тема обращения")
    body = models.TextField(verbose_name="Текст обращения")
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата обращения')
