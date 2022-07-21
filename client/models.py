from statistics import mode
from django.db import models

# Create your models here.


class Client(models.Model):
    nomclient = models.CharField(max_length=200,null=True)
    contact = models.CharField(max_length=200,null=True)
    date_creation = models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.nomclient
    