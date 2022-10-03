from rest_framework.routers import DefaultRouter
from rest.api.views import ProdsApiViewSet,CoordsProdsApiViewSet

router = DefaultRouter()

router.register(prefix='prods', basename='prods', viewset=ProdsApiViewSet)

router.register(prefix='coordsprods', basename='coordsprods', viewset=CoordsProdsApiViewSet)