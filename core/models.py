from django.db import models
from resources.models import Resource
from comments.models import Comment
from reviews.models import Review
from addresses.models import Address

# Create your models here.
class PontoTuristico(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    aproved = models.BooleanField(default=False)
    resource = models.ManyToManyField(Resource)
    comments = models.ManyToManyField(Comment)
    reviews = models.ManyToManyField(Review)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)
    def __str__(self):
        return self.name