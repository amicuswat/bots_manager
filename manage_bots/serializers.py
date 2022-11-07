from rest_framework import serializers

from .models import Balance


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = ('amount', 'moment')