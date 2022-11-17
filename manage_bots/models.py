from django.db import models
from django.utils import timezone

# Create your models here.


class Balance(models.Model):
    amount = models.IntegerField(verbose_name='Баланс:')
    moment = models.DateTimeField(verbose_name='Когда:',
                                  default=timezone.now,
                                  db_index=True)

    def __str__(self):
        return f'{self.amount} руб. - {self.moment}'

    class Meta:
        verbose_name = u'баланс'
        verbose_name_plural = u'балансы'


class TelegramGroup(models.Model):
    name = models.CharField(verbose_name='Название группы', max_length=200, blank=True)
    telegram_id = models.IntegerField(verbose_name='ID группы в Телеграм')
    is_notification_list = models.BooleanField(verbose_name='Получает уведомление', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'ТГ группа'
        verbose_name_plural = u'ТГ группы'


class Bot(models.Model):
    title = models.CharField(verbose_name='Название бота', max_length=100, unique=True)
    first_limit = models.IntegerField(verbose_name='Первый предел', default=5000)
    first_limit_delay = models.IntegerField(verbose_name='Периодичность уведомления в часах', default=12)
    critical_limit = models.IntegerField(verbose_name='Первый предел', default=2000)
    critical_limit_delay = models.IntegerField(verbose_name='Периодичность уведомления в часах', default=1)
    api_requests_interval = models.IntegerField(verbose_name='Частота обновления по АПИ в секундах', default=60)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u'бот'
        verbose_name_plural = u'боты'



