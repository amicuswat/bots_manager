from django.contrib import admin

from .models import Balance, Bot, TelegramGroup

# Register your models here.
admin.site.register([Balance, TelegramGroup, Bot])
