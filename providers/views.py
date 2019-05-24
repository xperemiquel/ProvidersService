from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from .serlializers import ProviderSelializer, ServiceAreaSerializer
from .models import Provider, ServiceArea

class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProviderSelializer

class ServiceAreaViewSet(viewsets.ModelViewSet):
    queryset = ServiceArea.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ServiceAreaSerializer
