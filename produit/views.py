from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def List_produit(request):
    return render(request,'produit/acceuil.html')
