from django.db import models

# Create your models here.
class Address(models.Model):
    line1 = models.CharField(max_length=150, null=True, blank=True)
    line2 = models.CharField(max_length=150, null=True, blank=True)
    city = models.CharField(max_length=150, null=True, blank=True)
    state = models.CharField(max_length=150, null=True, blank=True)
    
    def __str__(self):
        return self.line1
    