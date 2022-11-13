from django.contrib import admin

from .models import Balance, TelegramUser, Bot, TelegramGroup

# Register your models here.
admin.site.register([Balance, TelegramUser, TelegramGroup, Bot])
