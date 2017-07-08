# Django-base

#### Test 

Ces fichiers sont encore en développement et ne peuvent servir à quiconque pour le moment.
La version publique sera taguée V.1.0.0 lorsque prête.

### Présentation
Ce gabarit permet de créer facilement une application Django prête pour un déploiement avec Docker.

Il contient la version DEV et la version PROD avec les fichiers "settings", "dockerfile", "docker-compose" correspondants.

#### Version DEV
Dans cette version le volume est lié avec le répertoire courant pour refléter l'évolution du code en développement


#### fichier Dockerfile local

`
FROM python:3.4

ENV PYTHONUNBUFFERED 1
ENV PYTHON_SETTINGS_MODULE=src.settings.local

RUN mkdir /code
WORKDIR /code
ADD . /code/

RUN pip install -r requirements.txt \
    && python manage.py makemigrations \
    && python manage.py migrate \
    && python manage.py superuser \
    && python manage.py collectstatic --no-input

VOLUME .:/code

EXPOSE 8080:8000

CMD python manage.py runserver 0.0.0.0:8000 --settings=src.settings.local
`


#### fichier docker-compose local
Les volumes liés sont le répertoire courant et le volume nommé src-db

`
version: '3'
services:

  web:
    build: .
    image: webapp:dev
    container_name: webapp-dev

    command: python manage.py runserver 0.0.0.0:8000 --settings=src.settings.local

    volumes:
      - .:/code
      - src-db:/code

    ports:
      - "8080:8000"

volumes:
    src-db:
`

#### Version PROD
Dans cette version pas de lien avec le répertoire courant pour ne pas modifier la version même lors du développement du code


##### fichier Dockerfile Production

`
FROM python:3.4

ENV PYTHONUNBUFFERED 1
ENV PYTHON_SETTINGS_MODULE=src.settings.prod

RUN mkdir /code
WORKDIR /code
ADD . /code/

RUN pip install -r requirements.txt \
    && python manage.py makemigrations \
    && python manage.py migrate \
    && python manage.py superuser \
    && python manage.py collectstatic --no-input

EXPOSE 8081:8000

CMD python manage.py runserver 0.0.0.0:8000 --settings=src.settings.prod
`

##### fichier docker-compose version PROD

`
version: '3'
services:

  web:
    build:
      context: .
      dockerfile: Dockerfile_prod
    image: webapp:prod
    container_name: webapp-prod

    command: python manage.py runserver 0.0.0.0:8000 --settings=src.settings.prod

    volumes:
      - src-db:/code
    ports:
      - "8081:8000"

volumes:
    src-db:
`


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

Dernière version mise à jour le 2017-07-08
