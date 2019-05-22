from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Tournament(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="Название")
    url = models.CharField(max_length=255, verbose_name="Адрес", default="123321")
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания') #default=timezone.now
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name = "Создал"
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tournament_detail', args=[str(self.id)])
