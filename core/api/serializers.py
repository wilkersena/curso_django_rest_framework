from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from core.models import PontoTuristico
from resources.api.serializers import ResourceSerializer
from comments.api.serializers import CommentSerializer
from reviews.api.serializers import ReviewSerializer
from addresses.api.serializers import AddressSerializer
from datetime import date

class PontoTuristicoSerializer(ModelSerializer):
    resource = ResourceSerializer(many=True)
    comments = CommentSerializer(many=True)
    reviews = ReviewSerializer(many=True)
    address = AddressSerializer()
    data_hoje = SerializerMethodField()
    class Meta:
        model = PontoTuristico
        
        fields = ('id','data_hoje','name','photo','description','approved','resource', 'comments', 'reviews', 'address',)

    def get_data_hoje(self,obj):
        return date.today().strftime("%d/%m/%Y")
