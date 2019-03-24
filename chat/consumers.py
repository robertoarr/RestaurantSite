from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json


class RestaurantConsumer(WebsocketConsumer):

    def connect(self):
        self.room_group_name = 'restaurant_orders'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        pass

    # Receive message from room group
    def order_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'message': message
        }))
