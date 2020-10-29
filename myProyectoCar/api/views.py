from django.shortcuts import render

from myCarW.models import Insumos
from .serializers import InsumosSerializer
from rest_framework import generics

# Create your views here.

class InsumosViewSet(generics.ListCreateAPIView):
    queryset = Insumos.objects.all()
    serializer_class = InsumosSerializer