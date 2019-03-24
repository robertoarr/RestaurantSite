from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^restaurant_orders$', views.restaurant_orders, name='restaurant_orders'),
]
