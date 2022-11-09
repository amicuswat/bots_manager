from rest_framework import viewsets
from .models import Balance, TelegramUser
from .serializers import BalanceSerializer, MemberSerializer

# Create your views here.
class BalanceAPIView(viewsets.ModelViewSet):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer


class MemberAPIView(viewsets.ModelViewSet):
    queryset = TelegramUser.objects.all()
    serializer_class = MemberSerializer
