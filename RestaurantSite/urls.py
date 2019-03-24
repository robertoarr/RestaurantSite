from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from orders.urls import api_urlpatterns as order_v1
from chat.urls import urlpatterns as chat_v1


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^v1/', include(order_v1)),
    url(r'^v1/', include(chat_v1)),
]
