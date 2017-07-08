from django.conf.urls import url
from . import views as voiture_views

urlpatterns = [
    url(r'^$', voiture_views.home, name='home'),
    url(r'^conso', voiture_views.conso, name="conso"),
    url(r'^entretien', voiture_views.entretien, name='entretien'),
    url(r'^cout', voiture_views.cout, name='cout'),

]