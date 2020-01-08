from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico

class PontoTuristicoSerializer(ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ['id','name', 'description','photo']
        #fields = ('id','name', 'description','aproved','resource', 'comments', 'reviews', 'address',)