from django.core.management.base import BaseCommand, CommandError
from voiture.models import Voiture
from datetime import datetime

# TODO Tester la réponse de la commande


class Command(BaseCommand):

    message_ok = "La voiture par défaut a bien été créée"
    message_no = "La voiture par défaut existe déjà!"

    def handle(self, *args, **options):
        if not Voiture.objects.all().count() == 0:
            try:
                voiture = Voiture.objects.create(
                    marque = "Toyota",
                    type = "Camry Hybrid",
                    annee = 2007,
                    petit_nom = "Bleue",
                    odometre_depatr = 194694,
                    data_achat = datetime(2017, 6, 28),
                    cout_achat = 6600
                )

            except:
                raise CommandError("Problème de création de l'auto par défaut")

            # voiture.save()
            self.stdout.write(self.style.SUCCESS(self.message_ok))
        else:
            self.stdout.write(self.style.ERROR(self.message_no))
