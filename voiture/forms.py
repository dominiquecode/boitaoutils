from django.forms import ModelForm
from .models import Consommation, Entretien


class ConsommationForm(ModelForm):
    class Meta:
        model = Consommation
        fields = ["voiture", "odometre", "quantite_essence", "prix_litre"]


class EntretienForm(ModelForm):
    class Meta:
        model = Entretien
        fields = ['voiture', 'description', 'montant', 'date_frais']
