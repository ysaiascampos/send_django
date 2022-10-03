from dataclasses import field
from rest_framework.serializers import ModelSerializer
from rest.models import Prods, CoordsProds

class ProdsSerializer(ModelSerializer):
    class Meta:
        model = Prods
        fields = ['id','ref','zipcode','store','amount']

class CoordsProdsSerializer(ModelSerializer):
    class Meta:
        model = CoordsProds
        fields = ['id','ref_prods','lat','long']