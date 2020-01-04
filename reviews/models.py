from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    rate = models.DecimalField(max_digits=2,decimal_places=1,default=0.0 )
    date = models.DateTimeField(auto_now_add=True )


    def __str__(self):
        return self.user.username
