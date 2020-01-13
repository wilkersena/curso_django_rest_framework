from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from core.api.serializers import PontoTuristicoSerializer
from rest_framework.decorators import action
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
class PontoTuristicoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    
    serializer_class = PontoTuristicoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'name']
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


    def get_queryset(self):
        id = self.request.query_params.get('id',None)
        name = self.request.query_params.get('name',None)
        description = self.request.query_params.get('description',None)
        approved = self.request.query_params.get('approved',None)
        queryset = PontoTuristico.objects.all()

        if id:
            queryset = PontoTuristico.objects.filter(pk=id)
        if name:            
            queryset = queryset.filter(name__iexact=name)
        if description:
            queryset = queryset.filter(description__iexact=description)
        if approved:
            queryset = queryset.filter(approved__iexact=approved)
        
        return queryset

    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet,self).list( request, *args, **kwargs)

        
    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet,self).create( request, *args, **kwargs)

        
    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet,self).destroy( request, *args, **kwargs)

        
    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet,self).retrieve( request, *args, **kwargs)

        
    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet,self).update( request, *args, **kwargs)

        
    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet,self).partial_update( request, *args, **kwargs)

    @action(methods=['get'], detail=False)
    def teste(self,request):
        pass

