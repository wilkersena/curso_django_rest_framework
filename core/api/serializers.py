from rest_framework.serializers import HyperlinkedModelSerializer
from core.models import PontoTuristico

class PontoTuristicoSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ['id','name', 'description']
        #fields = ('id','name', 'description','aproved','resource', 'comments', 'reviews', 'address')