from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serlializers import ProviderSelializer, ServiceAreaSerializer, CheckServiceAreaSerializer, Provider, ServiceArea


class ProviderViewSet(ModelViewSet):
    queryset = Provider.objects.all()
    permission_classes = [
        AllowAny
    ]
    serializer_class = ProviderSelializer

class ServiceAreaViewSet(ModelViewSet):
    queryset = ServiceArea.objects.all()
    permission_classes = [
        AllowAny
    ]
    serializer_class = ServiceAreaSerializer

class CheckServiceAreaApiView(ViewSet):
    queryset = ServiceArea.objects.all()
    permission_classes = [
        AllowAny
    ]
    serializer_class = CheckServiceAreaSerializer

    def get(self, request):
    #     return Response({'result': 'OK'})
    # def get(self, request):
    #     serializer = CheckServiceAreaSerializer(data=request.query_params)
    #     if serializer.is_valid():
    #         data = serializer.validated_data
    #         print(data) # process data
    #         
    #     else:
    #         return Response({'result': 'Invalid Input'})
        
        


