from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import Commande



class CommandeForm(ModelForm):
    class meta:
        model=Commande
        fields='__all__'