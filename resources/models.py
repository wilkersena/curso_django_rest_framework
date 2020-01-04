from django.db import models

# Create your models here.
class Resource(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    operation_hour = models.TextField()
    minimal_age = models.IntegerField()

    def __str__(self):
        return self.name

