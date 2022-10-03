from rest_framework.viewsets import ModelViewSet
from rest.models import Prods
from rest.api.serializers import ProdsSerializer

class ProdsApiViewSet(ModelViewSet):
    serializer_class = ProdsSerializer
    queryset = Prods.objects.all()