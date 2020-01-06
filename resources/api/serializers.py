from rest_framework.serializers import ModelSerializer
from resources.models import Resource

class ResourceSerializer(ModelSerializer):
    class Meta:
        model = Resource
        fields = ['id','name','description', 'operation_hour', 'minimal_age']