from rest_framework import serializers

from .models import Balance, TelegramOrganisation, TelegramUser


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = ('amount', 'moment', 'organisation')


class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramOrganisation
        fields = ('id', 'title', 'chat_id')


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = ('id', 'telegram_id', 'organisation')
