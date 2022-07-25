from . import views
from django.urls import path


urlpatterns = [
    path('',views.list_commande),
    path('ajout_commande/',views.Ajouter_commande ,name='ajout_commande'),
    #path('modifier_commande/<str:pk>',views.modifier_commande ,name='modifier_commande'),
    #path('supprimer_commande/<str:pk>',views.supprimer_commande ,name='supprimer_commande')
]
