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
    title = models.CharField(verbose_name='Название бота:',
                             max_length=100, unique=True)
    first_limit = models.IntegerField(
        verbose_name='Первый порог срабатывания автоматики:',
        default=5000,
        help_text='Если баланс в РУБЛЯХ опустится ниже этого значения '
                  'бот будет отправлять напоминания о необходимости оплаты'
    )
    first_limit_delay = models.IntegerField(
        verbose_name='Повторное уведомление при первом пороге',
        default=12,
        help_text='Интервал в ЧАСАХ, через который бот будет отправлять '
                  'повторное уведомление при первом пороге'
    )
    critical_limit = models.IntegerField(
        verbose_name='Второй порог срабатывания автоматики',
        default=2000,
        help_text='Если баланс в РУБЛЯХ опустится ниже этого значения бот '
                  'будет отправлять напоминания о необходимости оплаты чаще'
    )
    critical_limit_delay = models.IntegerField(
        verbose_name='Повторное уведомление при втором пороге',
        default=1,
        help_text='Интервал в ЧАСАХ, через который бот будет отправлять '
                  'повторное уведомление при втором пороге'
    )
    api_requests_interval = models.IntegerField(
        verbose_name='Частота запроса баланса по АПИ',
        default=60,
        help_text='Инетрвал в СЕКУНДАХ, через который бот '
                  'запрашивает обновление данных о балансе по АПИ'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u'бот'
        verbose_name_plural = u'боты'



