from rest_framework import viewsets
from .models import Balance, Bot, TelegramGroup
from .serializers import BalanceSerializer, BotSerializer, GroupSerializer

# Create your views here.
class BalanceAPIView(viewsets.ModelViewSet):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer


class GroupAPIView(viewsets.ModelViewSet):
    queryset = TelegramGroup.objects.all()
    serializer_class = GroupSerializer


class BotAPIView(viewsets.ModelViewSet):
    queryset = Bot.objects.all()
    serializer_class = BotSerializer