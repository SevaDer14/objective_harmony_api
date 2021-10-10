from django.shortcuts import render
from .serializers import SpectrumSerializer
from rest_framework import viewsets
from .models import Spectrum


class SpectrumView(viewsets.ModelViewSet):
    serializer_class = SpectrumSerializer
    queryset = Spectrum.objects.all()
