from rest_framework import serializers
from .models import Spectrum

class SpectrumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spectrum
        fields = ("id", "name")
