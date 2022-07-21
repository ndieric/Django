from audioop import maxpp
from django.db import models

from client.models import Client
from produit.models import Produit

# Create your models here.


class Commande(models.Model):
    STATUS=(('livre','livre'),('non livre','non livre'),('en instance','en instance'))
    date_creation=models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField(max_length=200,null=True,choices=STATUS)
    client=models.ForeignKey(Client,null=True,on_delete=models.SET_NULL)
    Produit=models.ForeignKey(Produit,null=True,on_delete=models.SET_NULL)
    
    
    def __str__(self):
        return self.status
    