from django.db import models
from django.utils import timezone

# Create your models here.


class Balance(models.Model):
    amount = models.IntegerField(verbose_name='Баланс:')
    moment = models.DateTimeField(verbose_name='Когда:',
                                  default=timezone.now,
                                  db_index=True)


class TelegramUser(models.Model):
    name = models.CharField(verbose_name='ФИО', max_length=200, blank=True)
    tg_name = models.CharField(verbose_name='Ник в ТГ', max_length=50, blank=True)
    telegram_id = models.IntegerField(verbose_name='ID участника в Телеграм')
    is_bot_user = models.BooleanField(verbose_name='Видит баланс', default=True)
    is_notification_list = models.BooleanField(verbose_name='Получает уведомление', default=False)
