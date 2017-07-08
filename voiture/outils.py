from .models import Entretien, Consommation
from django.db.models import Max, Sum
from datetime import datetime


class CalculCouts:
    """
    Tous les calculs de coût pour une voiture particulière

    """
    def __init__(self, voiture):
        self._voiture = voiture
        self._cout_consos = 0
        self._liste_entretiens = []
        self._liste_consos = []

    def get_voiture(self):
        return self._voiture

    @property
    def date_achat(self):
        return self._voiture.date_achat

    @property
    def annee_achat(self):
        return datetime(self.date_achat).year

    @property
    def prix_achat(self):
        return self._voiture.cout_achat

    @property
    def odo_depart(self):
        return self._voiture.odometre_depart

    def get_odo_actuel(self):
        valeur = self._voiture.consommation_set.aggregate(odo_max=Max('odometre'))
        if valeur.get('odo_max') is not None:
            return valeur.get('odo_max')
        else:
            return self._voiture.odometre_depart

    def get_km_total_parcourus(self):
        if self._voiture.odometre_depart is not None and self.get_odo_actuel():
            return self.get_odo_actuel() - self._voiture.odometre_depart
        else:
            return 0

    def get_km_intermediaire_parcourus(self):
        list_2_dernier = self.get_liste_consos()[0:2]
        print(list_2_dernier)
        return list_2_dernier

    def get_liste_consos(self):
        self._liste_consos = list(Consommation.objects.all().filter(voiture_id=self._voiture))
        return self._liste_consos

    def get_cout_carburant(self):
        self._cout_consos = 0
        consos = list(Consommation.objects.all().filter(voiture_id=self._voiture))
        for conso in consos:
            cout = conso.quantite_essence * conso.prix_litre
            self._cout_consos += cout
        return self._cout_consos

    def get_conso_moyenne(self):
        valeur = self._voiture.consommation_set.aggregate(essence_max=Sum('quantite_essence'))
        if valeur.get('essence_max') is not None and self.get_km_total_parcourus() > 0:
            qte_totale = valeur.get('essence_max')
            return '{0:.2f}'.format(qte_totale / self.get_km_total_parcourus() * 100)
        else:
            return 0

    def get_liste_entretiens(self):
        self._liste_entretiens = Entretien.objects.all().filter(voiture_id=self._voiture)
        return self._liste_entretiens

    def get_nb_entretien(self):
        return Entretien.objects.all().filter(voiture_id=self._voiture).count()

    def get_cout_entretien(self):
        valeur = self._voiture.entretien_set.aggregate(total=Sum('montant'))
        if valeur.get('total') is not None:
            return valeur.get('total')
        else:
            return 0

    def get_cout_exploitation(self):
        return self.get_cout_carburant() + self.get_cout_entretien()

    def get_cout_complet(self):
        return self.get_cout_exploitation() + self.prix_achat

    def get_cout_moyen_annuel(self):
        annee_actuelle = int(datetime.now().year)
        nb_annee = annee_actuelle - 2017 + 1
        return '{0:.2f}'.format(self.get_cout_complet() / nb_annee)
