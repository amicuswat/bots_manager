from rest_framework import generics
from django.shortcuts import render
from .models import Balance
from .serializers import BalanceSerializer

# Create your views here.
class BalanceAPIView(generics.ListCreateAPIView):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer




