from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from core.models import PontoTuristico
from resources.models import Resource
from resources.api.serializers import ResourceSerializer
from comments.api.serializers import CommentSerializer
from reviews.api.serializers import ReviewSerializer
from addresses.api.serializers import AddressSerializer
from addresses.models import Address
from datetime import date

class PontoTuristicoSerializer(ModelSerializer):
    resource = ResourceSerializer(many=True)
    comments = CommentSerializer(many=True,read_only=True)
    reviews = ReviewSerializer(many=True,read_only=True)
    address = AddressSerializer()
    data_hoje = SerializerMethodField(read_only=True)
    class Meta:
        model = PontoTuristico        
        fields = ('id','data_hoje','name','photo','description','approved','resource', 'comments', 'reviews', 'address',)
        read_only_fields = ['comments', 'reviews']

    def get_data_hoje(self,obj):
        return date.today().strftime("%d/%m/%Y")

    def create(self, validated_data):
        resources = validated_data.pop('resource')
        address = validated_data.pop('address')
        ponto = PontoTuristico.objects.create(**validated_data)
        for resource in resources:
            rsc = Resource.objects.create(**resource)
            ponto.resource.add(rsc)
        ad = Address.objects.create(**address)
        ponto.address = ad
        ponto.save()

        return ponto
