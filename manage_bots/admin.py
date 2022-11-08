from django.contrib import admin

from .models import Balance, TelegramOrganisation, TelegramUser

# Register your models here.
admin.site.register([Balance, TelegramOrganisation, TelegramUser])
