from rest_framework import viewsets
from .models import Balance, TelegramUser, Bot
from .serializers import BalanceSerializer, MemberSerializer, BotSerializer

# Create your views here.
class BalanceAPIView(viewsets.ModelViewSet):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer


class MemberAPIView(viewsets.ModelViewSet):
    queryset = TelegramUser.objects.all()
    serializer_class = MemberSerializer


class BotAPIView(viewsets.ModelViewSet):
    queryset = Bot.objects.all()
    serializer_class = BotSerializer