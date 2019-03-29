import json

import channels.layers
from rest_framework import serializers
from asgiref.sync import async_to_sync

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    created = serializers.SerializerMethodField()
    test = serializers.BooleanField(write_only=True, default=False)

    class Meta:
        model = Order
        fields = ('id', 'phone_number', 'address', 'name', 'food_order', 'created', 'test')

    def get_created(self, obj):
        return obj.created.strftime("%Y/%m/%d %H:%M:%S")


class ListOrderSerializer(serializers.Serializer):
    search = serializers.CharField(required=False)

    def list(self):
        orders = Order.objects.all().order_by('created')
        if self.validated_data.get('search'):
            orders = orders.filter(name__icontains=self.validated_data.get('search'))
        return OrderSerializer(orders, many=True).data


class CreateOrderSerializer(OrderSerializer):

    def create_order(self):
        order = Order(phone_number=self.validated_data.get('phone_number'),
                      address=self.validated_data.get('address'),
                      name=self.validated_data.get('name'),
                      food_order=self.validated_data.get('food_order')
                      )
        order.save()
        resp = OrderSerializer(order).data
        channel_layer = channels.layers.get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'restaurant_orders',
            {
                'type': "order_message",
                'message': resp
            }
        )
        return resp
