from rest_framework import viewsets
from .models import Balance, TelegramOrganisation, TelegramUser
from .serializers import BalanceSerializer, OrganisationSerializer, MemberSerializer

# Create your views here.
class BalanceAPIView(viewsets.ModelViewSet):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer


class OrganisationAPIView(viewsets.ModelViewSet):
    queryset = TelegramOrganisation.objects.all()
    serializer_class = OrganisationSerializer


class MemberAPIView(viewsets.ModelViewSet):
    queryset = TelegramUser.objects.all()
    serializer_class = MemberSerializer