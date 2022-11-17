from rest_framework import serializers

from .models import Balance, Bot, TelegramGroup


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = ('amount', 'moment')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramGroup
        fields = ('id', 'name', 'telegram_id', 'is_notification_list')


class BotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bot
        fields = ('id', 'first_limit', 'first_limit_delay', 'critical_limit', 'critical_limit_delay')
