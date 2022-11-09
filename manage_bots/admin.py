from django.contrib import admin

from .models import Balance, TelegramUser, Bot

# Register your models here.
admin.site.register([Balance, TelegramUser, Bot])
