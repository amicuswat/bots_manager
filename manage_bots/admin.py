from django.contrib import admin

from .models import Balance, TelegramUser

# Register your models here.
admin.site.register([Balance, TelegramUser])
