from dataclasses import field
from rest_framework.serializers import ModelSerializer
from rest.models import Prods

class ProdsSerializer(ModelSerializer):
    class Meta:
        model = Prods
        fields = ['id','ref','zipcode','store','amount']