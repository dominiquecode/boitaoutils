# Django-base

#### Test 

Ces fichiers sont encore en développement et ne peuvent servir à quiconque pour le moment.
La version publique sera taguée V.1.0.0 lorsque prête.

### Présentation
Ce gabarit permet de créer facilement une application Django prête pour un déploiement avec Docker.

Il contient la version DEV et la version PROD avec les fichiers "settings", "dockerfile", "docker-compose" correspondants.

#### CI/CD

Cette application fonctionne en mode autobuild avec Docker Hub (domidocker/boitaoutils)
La procédure reste standard : 
* mise à jour dans Pycharm
* commit les modifications
* push vers le repos Github
* l'image dans Docker Hub se met à jour en automatique

### Remarques
Tous les fichiers sont publics 
Aucune restriction sur leur utilisation. Lire la licence au besoin.
Cette application sert à l'apprentissage de Python et Django.
