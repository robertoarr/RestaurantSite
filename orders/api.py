from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import ListOrderSerializer, CreateOrderSerializer


class OrderViewSet(viewsets.GenericViewSet):

    def list(self, request):
        serializer = ListOrderSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        response = serializer.list()
        return Response({'data': response})

    def create(self, request):
        serializer = CreateOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = serializer.create_order()
        return Response({'data': response})
