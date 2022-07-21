from django.db import models
from django.forms import IntegerField

# Create your models here.

class Tag(models.Model):
    nomproduit = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.nomproduit
    
    
class Produit(models.Model):
    nomproduit = models.CharField(max_length=200,null=True)
    quantite=models.IntegerField(max_length=200,null=True)
    prix=models.FloatField(max_length=200,null=True)
    data_creation=models.DateTimeField(auto_now_add=True,null=True)
    tag=models.ManyToManyField(Tag)
    
    
    def __str__(self):
        return self.nomproduit
    