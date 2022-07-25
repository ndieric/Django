from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import CommandeForm
from .models import Commande

# Create your views here.

def list_commande(request):
    return render(request,'commande/acceuil_commande.html')

def Ajouter_commande(request):
    
    model=CommandeForm()
    if request.method=='POST':
        form=CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'../commande/ajouter_commande.html',context)

#def modifier_commande(request,pk):
    #commande=Commande.objects.get(id=pk)
    #model=CommandeForm(instance=commande)
    #if request.method=='POST':
        #form=CommandeForm(request.POST,instance=commande)
        #if form.is_valid():
           # form.save()
           # return redirect('/')
    #context={'form':form}
    #return render(request,'../commande/ajouter_commande.html',context)

#def supprimer_commande(request,pk):
    #commande=Commande.objects.get(id=pk)
    #if request.method=='POST':
       # commande.delete()
       # return redirect('/')
    #context={'item':commande}
    #return render(request,'commande/supprimer_commande.html',context)
