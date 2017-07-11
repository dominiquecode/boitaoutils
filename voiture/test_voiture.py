# fichier de test de l'application Voiture

from django.test import TestCase
from .models import Voiture, Consommation
from django.utils.timezone import datetime
from .outils import CalculCouts


class VoitureTestCase(TestCase):

    def setUp(self):
        self.voiture = Voiture.objects.create(
            id=1,
            marque="Tesla",
            type= "modèle 3",
            annee=2007,
            petit_nom="choupette",
            odometre_depart=1000,
            date_achat=datetime(2010,1,1),
            cout_achat=10000
        )

        self.conso = Consommation.objects.create(
            voiture=self.voiture,
            odometre=1500,
            quantite_essence=50,
            prix_litre=1.00
        )

        self.calcul = CalculCouts(self.voiture)

    def test_voiture_info(self):
        self.assertEqual(self.voiture.marque, "Tesla")
        self.assertEqual(self.voiture.annee, 2007)

    def test_odo_actuel(self):
        odo = self.calcul.get_odo_actuel()
        self.assertEqual(odo, 1500)

    def test_km_parcourus(self):
        self.assertEqual(self.calcul.get_km_total_parcourus(), 500)

    def test_list_conso(self):
        liste = list(self.calcul.get_liste_consos())
        self.assertEqual(len(self.calcul.get_liste_consos()), 1)

    def test_cout_carburant(self):
        self.assertEqual(self.calcul.get_cout_carburant_total(), 50)

    def test_quantite_carburant_total(self):
        self.assertEqual(self.calcul.get_qte_carburant_totale(), 50)

    def test_cout_entretien_zero(self):
        self.assertEqual(self.calcul.get_cout_entretien(), 0)

    def test_cout_exploitation(self):
        self.assertEqual(self.calcul.get_cout_exploitation(), 50)

    def test_cout_complet(self):
        self.assertEqual(self.calcul.get_cout_complet(), 10050)

    def test_cout_moyen_annuel(self):
        self.assertEqual(self.calcul.get_cout_moyen_annuel(), 10050.00)

    def test_km_intermediaire_parcourus(self):
        Consommation.objects.create(voiture=self.voiture,
                                    odometre=2000,
                                    quantite_essence=50,
                                    date_conso=datetime(2010,2,1),
                                    prix_litre=1.00)
        self.assertEqual(len(self.calcul.get_liste_consos()), 2)
        self.assertEqual(self.calcul.get_km_total_parcourus(), 1000)
        self.assertEqual(self.calcul.get_cout_carburant_total(), 100)
        self.assertEqual(self.calcul.get_odo_precedent(), 1500)
        self.assertEqual(self.calcul.get_odo_actuel(), 2000)
        self.assertEqual(self.calcul.get_qte_carburant_totale(), 100)
        self.assertEqual(self.calcul.get_conso_moyenne(), 5.00)





