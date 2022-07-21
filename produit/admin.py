from django.contrib import admin

from produit.models import Produit, Tag

# Register your models here.


admin.site.register(Produit)
admin.site.register(Tag)