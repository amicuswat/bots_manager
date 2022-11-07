from django.db import models
from django.utils import timezone

# Create your models here.
class Balance(models.Model):
    amount = models.IntegerField(verbose_name='Баланс:')
    moment = models.DateTimeField(verbose_name='Когда:',
                                  default=timezone.now,
                                  db_index=True)
