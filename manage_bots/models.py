from django.db import models
from django.utils import timezone

# Create your models here.
class TelegramOrganisation(models.Model):
    title = models.CharField(verbose_name='Название организации', max_length=200)
    chat_id = models.IntegerField(verbose_name='ID группы в Телеграм')

    def __str__(self):
        return self.title


class Balance(models.Model):
    amount = models.IntegerField(verbose_name='Баланс:')
    moment = models.DateTimeField(verbose_name='Когда:',
                                  default=timezone.now,
                                  db_index=True)
    organisation = models.ForeignKey(
        TelegramOrganisation,
        verbose_name='Компания-клиент',
        on_delete=models.CASCADE
    )


class TelegramUser(models.Model):
    telegram_id = models.IntegerField(verbose_name='ID участника в Телеграм')
    organisation = models.ForeignKey(
        TelegramOrganisation,
        verbose_name='Компания пользователя',
        on_delete=models.CASCADE,
        related_name='members'
    )