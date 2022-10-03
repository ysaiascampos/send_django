from rest_framework.routers import DefaultRouter
from rest.api.views import ProdsApiViewSet

router_prods = DefaultRouter()

router_prods.register(prefix='rest', basename='rest', viewset=ProdsApiViewSet)