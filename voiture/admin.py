from django.contrib import admin
from .models import Voiture, Consommation, Entretien


# Register your models here.
class VoitureAdmin(admin.ModelAdmin):
    list_display = ('petit_nom', 'marque', 'type', 'annee', 'cout_achat')

admin.site.register(Voiture, VoitureAdmin)


class ConsommationAdmin(admin.ModelAdmin):
    list_display = ('voiture', 'odometre', 'date_conso', 'quantite_essence', 'prix_litre')


admin.site.register(Consommation, ConsommationAdmin)


class EntretienAdmin(admin.ModelAdmin):
    list_display = ('voiture', 'description', 'date_frais', 'montant')

admin.site.register(Entretien, EntretienAdmin)
