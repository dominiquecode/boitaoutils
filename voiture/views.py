from django.shortcuts import render, get_object_or_404
from .models import Voiture
from .outils import CalculCouts
from .forms import ConsommationForm, EntretienForm


# Create your views here.
def home(request):
    return render(request, 'voiture_home.html', {})


def conso(request, pk_voiture=1):
    """
    Procédure de calcul pour tous les paramètres d'affichage
    :param request:
    :param pk_voiture: valeur par défaut = 1
    :return:
    """
    # données de la voiture surveillée
    voiture = get_object_or_404(Voiture, pk=pk_voiture)
    voiture_actuelle = CalculCouts(voiture)

    if request.method == "POST":
        form = ConsommationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ConsommationForm()

    # passation des valeurs dans le contexte
    context = { 'voiture': voiture_actuelle.get_voiture(),
                'odometre_actuel': voiture_actuelle.get_odo_actuel(),
                'odometre_precedent': voiture_actuelle.get_odo_precedent(),
                'parcours': voiture_actuelle.get_km_total_parcourus(),
                'conso': '{0:.2f}'.format(voiture_actuelle.get_conso_moyenne()),
                'couts_carburant': '{0:.2f}'.format(voiture_actuelle.get_cout_carburant_total()),
                'form': form,
                }

    # remplir le template
    return render(request, 'voiture_conso.html', context)


def entretien(request, pk_voiture=1):
    """
    Gestion des entretiens de l'auto

    :param request:
    :param pk_voiture:
    :return:
    """

    # données de la voiture surveillée
    voiture = get_object_or_404(Voiture, pk=pk_voiture)
    voiture_actuelle = CalculCouts(voiture)

    if request.method == 'POST':
        form = EntretienForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EntretienForm()

    # passation des valeurs dans le contexte
    context = {'voiture': voiture_actuelle.get_voiture(),
                'odometre_actuel': voiture_actuelle.get_odo_actuel(),
                'parcours': voiture_actuelle.get_km_total_parcourus(),
                'nb_entretien': voiture_actuelle.get_nb_entretien(),
                'cout_entretien': voiture_actuelle.get_cout_entretien(),
                'form': form,
               }
    return render(request, 'voiture_entretien.html', context)


def cout(request, pk_voiture=1):
    """
    Récapitulatif des coûts d'entretien et de carburant de l'auto

    :param request:
    :param pk_voiture: valeur par défaut 1 (Choupinette)
    :return:
    """
    # données de la voiture surveillée
    voiture = get_object_or_404(Voiture, pk=pk_voiture)
    voiture_actuelle = CalculCouts(voiture)

    context = {'voiture': voiture_actuelle.get_voiture(),
               'odometre_actuel': voiture_actuelle.get_odo_actuel(),
               'parcours': voiture_actuelle.get_km_total_parcourus(),
               'couts_carburant': '{0:.2f}'.format(voiture_actuelle.get_cout_carburant_total()),
               'conso': '{0:.2f}'.format(voiture_actuelle.get_conso_moyenne()),
               'liste_entretiens': voiture_actuelle.get_liste_entretiens(),
               'cout_entretien': voiture_actuelle.get_cout_entretien(),
               'cout_exploitation': '{0:.2f}'.format(voiture_actuelle.get_cout_exploitation()),
               'cout_total': '{0:.2f}'.format(voiture_actuelle.get_cout_complet()),
               'nb_entretien': voiture_actuelle.get_nb_entretien(),
               'cout_moyen_annuel': '{0:.2f}'.format(voiture_actuelle.get_cout_moyen_annuel()),
               }
    return render(request, 'voiture_cout.html', context)


