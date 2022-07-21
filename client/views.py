from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from commande.models import Commande
from client.models import Client;

# Create your views here.

def Home(request):
    commande=Commande.objects.all()
    client=Client.objects.all()
    context={'commandes':commande,'clients':client}
    return render(request,'Client/acceuil_client.html',context)