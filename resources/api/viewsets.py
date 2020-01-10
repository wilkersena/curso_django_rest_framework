from rest_framework.viewsets import ModelViewSet 
from resources.models import Resource
from resources.api.serializers import ResourceSerializer

class ResourceViewSet(ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    filter_fields = ['name', 'description']