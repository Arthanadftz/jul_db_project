from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

#from django.utils import timezone
from datetime import date

# Create your models here.
class CustomUser(AbstractUser):
    date_of_birth = models.DateTimeField(verbose_name='Дата рождения', default=date.today)
    full_name = models.CharField(max_length=255, verbose_name='Фамилия', null=True)
    phone_no = models.CharField(max_length=255, verbose_name='Контактный телефон', default='+7-499-555-55-55')

    PILOT = 'ПИ'
    VIEWER = 'ПО'
    PARTNER = 'ПА'
    MEMBER = 'УЧ'

    ROLE_CHOICES = (
        (PILOT, 'Пилот'),
        (MEMBER, 'Член команды'),
        (PARTNER, 'Партнер'),
        (VIEWER, 'Зритель'),

    )
    user_role = models.CharField(max_length=2,
        choices=ROLE_CHOICES,
        default=VIEWER,
        verbose_name='Роль пользователя'
    )


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    avatar = models.ImageField(upload_to='profile_pics', default='default.jpg', verbose_name='Аватар')

    def __str__(self):
        return f'Профиль пользователя - {self.user.username}'


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
