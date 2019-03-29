from django.test import TestCase
from orders.models import Order


class OrderTestCase(TestCase):
    def setUp(self):
        self.name = "Roberto"
        Order.objects.create(phone_number="5541743906",
                             address="Av. 123 Col. BCD, Del. G.A.M.",
                             name=self.name,
                             food_order="Menu 1")
        Order.objects.create(phone_number="5541743906",
                             address="Av. 123 Col. BCD, Del. G.A.M.",
                             name=self.name,
                             food_order="Menu 2")

    def test_order_created(self):
        orders = Order.objects.filter(name=self.name)
        for order in orders:
            self.assertEqual(order.name, self.name)
