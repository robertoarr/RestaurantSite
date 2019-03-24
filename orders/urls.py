from . import api
from rest_framework import routers

router = routers.SimpleRouter()
router.trailing_slash = '/?'
router.register(r'order', api.OrderViewSet, base_name='v1_order')

api_urlpatterns = router.urls
