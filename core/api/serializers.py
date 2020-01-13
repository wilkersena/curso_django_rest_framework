from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from resources.api.serializers import ResourceSerializer
from comments.api.serializers import CommentSerializer

class PontoTuristicoSerializer(ModelSerializer):
    class Meta:
        model = PontoTuristico
        
        fields = ('id','name','photo','description','aproved','resource', 'comments', 'reviews', 'address',)