import uuid

from django.db import models


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=400)
    name = models.CharField(max_length=200)
    food_order = models.CharField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)
