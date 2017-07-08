from django.db import models
from django.utils import timezone


# Create your models here.
class Voiture(models.Model):
    marque = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    annee = models.IntegerField()
    petit_nom = models.CharField(max_length=20)
    odometre_depart = models.IntegerField()
    date_achat = models.DateField(default=timezone.now)
    cout_achat = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.petit_nom


class Consommation(models.Model):
    voiture = models.ForeignKey(Voiture)
    odometre = models.IntegerField()
    quantite_essence = models.DecimalField(max_digits=5, decimal_places=2)
    date_conso = models.DateField(default=timezone.now)
    prix_litre = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.voiture.petit_nom


class Entretien(models.Model):
    voiture = models.ForeignKey(Voiture)
    description = models.CharField(max_length=100)
    montant = models.DecimalField(max_digits=5, decimal_places=2)
    date_frais = models.DateField(default=timezone.now)

    def __str__(self):
        return self.voiture.petit_nom

