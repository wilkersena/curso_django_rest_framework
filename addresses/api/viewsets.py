from rest_framework.viewsets import ModelViewSet
from addresses.models import Address
from addresses.api.serializers import AddressSerializer

class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer