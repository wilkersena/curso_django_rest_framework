from rest_framework.viewsets import ModelViewSet
from comments.api.serializers import CommentSerializer
from comments.models import Comment
from rest_framework import filters

class CommentViewSet(ModelViewSet):
        queryset = Comment.objects.all()
        serializer_class = CommentSerializer
        filter_backends = [filters.SearchFilter]
        search_fields = ['date','approved']
        filter_fields = ['date']