from rest_framework import serializers
from .models import Provider, ServiceArea

class ProviderSelializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = '__all__'

class ServiceAreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceArea
        fields = '__all__'

class CheckServiceAreaSerializer(serializers.Serializer):
    lat = serializers.FloatField()
    lng = serializers.FloatField()

