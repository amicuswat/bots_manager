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


class TelegramGroup(models.Model):
    name = models.CharField(verbose_name='Название группы', max_length=200, blank=True)
    telegram_id = models.IntegerField(verbose_name='ID группы в Телеграм')
    is_notification_list = models.BooleanField(verbose_name='Получает уведомление', default=False)

    def __str__(self):
        return self.name


class Bot(models.Model):
    title = models.CharField(verbose_name='Название бота', max_length=100, unique=True)
    type = models.CharField(verbose_name='Тип бота', max_length=50)
    first_limit = models.IntegerField(verbose_name='Первый предел', default=5000)
    first_limit_delay = models.IntegerField(verbose_name='Периодичность уведомления в часах', default=12)
    critical_limit = models.IntegerField(verbose_name='Первый предел', default=2000)
    critical_limit_delay = models.IntegerField(verbose_name='Периодичность уведомления в часах', default=1)



