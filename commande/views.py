from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def list_commande(request):
    return render(request,'commande/acceuil_commande.html')
