from rest_framework import serializers

from .models import Balance, TelegramUser


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = ('amount', 'moment')


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = ('id', 'telegram_id', 'is_bot_user', 'is_notification_list')
