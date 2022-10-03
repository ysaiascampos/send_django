from rest_framework.viewsets import ModelViewSet
from rest.models import Prods, CoordsProds
from rest.api.serializers import ProdsSerializer, CoordsProdsSerializer

class ProdsApiViewSet(ModelViewSet):
    serializer_class = ProdsSerializer
    queryset = Prods.objects.all()

class CoordsProdsApiViewSet(ModelViewSet):
    serializer_class = CoordsProdsSerializer
    queryset = CoordsProds.objects.all()