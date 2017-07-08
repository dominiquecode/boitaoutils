import os  # pour travailler avec les fichiers (lecture écriture)
import sys
import shutil  # pour travailler avec les fichiers (copier, déplacer, renomer, supprimer)
import datetime  # pour travailler avec les dates
# import ftplib as ftp  # pour travailler avec les connexions serveur
from easygui import *  # pour afficher les fenêtres de travail de l'application


def photos_move(source, destination):

    """
    Procédure principale de l'application

    Déplacer les photos qui se trouent dans le répertoire source
    vers le répertoire destination

    Afficher le nombre de photos déplacées

    """
    valides_extentions = ["jpg", "JPG", "jpeg", "MOV", "PNG", "png"]
    source_folder = source # get_folder('source')
    destination_folder = destination # get_folder('destination')
    cpt = 0

    # check selected folder
    if destination_folder is None or source_folder is None:
        sys.exit(0)

    # confirm folder choice
    if confirmation(source_folder, destination_folder):

        # move to source folder
        os.chdir(source_folder)

        # read all files (video/photo) of the current folder
        files_list = os.listdir(os.getcwd())
        for file in files_list:
            if file.rpartition(".")[2] in valides_extentions:
                creation_date = find_creation_date(file)
                print("Fichier : {} - {}".format(file, creation_date))
                cpt += 1
                create_under_folder(file, destination_folder)

                # move file in destination folder
                move_to_destination_folder(file,
                                           creation_date,
                                           source_folder,
                                           destination_folder)
                # afficher le nombre de fichiers déplacés
        display_file_number(source_folder, cpt)
    else:
        msgbox('La procédure est annulée, pas de modification de photo', 'Arrêt de procédure')


def display_file_number(source_folder, count):
    """
    retourne un message avec le nombre de photos déplacées
    durant la précédure

    :param source_folder:
    :param count:
    :return: NIL
    """
    title = "Les résultats de l'opération"
    if count == 0:
        message = "Aucun fichier déplacé \nLe répertoire {} est vide".format(source_folder)
    else:
        message = "Nombre de fichiers déplacés : {}".format(count)
    print(title, message)
    msgbox(message, title)


def move_to_destination_folder(file, creation_date, source_folder, destination_folder):
    """
    Déplacer les fichiers photos dans un répertoire
    :param file: le chemin complet du file (basestring)
    :param creation_date: la date de création du file (date)
    :param source_folder: le chemin complet du répertoire source (basestring)
    :param destination_folder: le chemin complet du répertoire destination (basestring)

    """
    source = os.path.join(source_folder, file)
    destination = os.path.join(destination_folder, creation_date[:4], creation_date, file)
    shutil.move(source, destination)
    print('Déplacement du file ' + source + '\nvers ' + destination + '\n')


def create_under_folder(file, destination_folder):
    """
    Construire un sous-répertoire pour y déplacer les fichiers photos
    le classement se fait en fonctione de l'année et du jour de création
    de la photo
    :param file: le chemin complet du file (basestring)
    :param destination_folder: le chemin complet du répertoire de destination (basestrinb)

    """
    creation_date = find_creation_date(file)
    year = creation_date[:4]

    print('----------------------------')
    print('Repertoire année : {0} repertoire jour : {1} '.format(year, creation_date))

    year_folder = os.path.join(destination_folder, year)

    # create year folder if not exist
    if not os.path.exists(year_folder):
        print('Création du répertoire année : ' + year_folder)
        os.makedirs(year_folder)
    else:
        print(('Le répertoire année ' + year_folder + ' existe déjà!'))

    # création du répertoire jour s'il n'existe pas
    destination_folder_path = year_folder + '/' + creation_date
    if not os.path.exists(destination_folder_path):
        print('Création du répertoire jour : ' + destination_folder_path)
        os.makedirs(destination_folder_path)
    else:
        print('Le répertoire jour ' + destination_folder_path + ' existe déjà')


def confirmation(source_folder, destination_folder):
    """
    message de confirmation du choix des répertoires
    si CANCEL est cliqué, l'application s'arrête
    si OK est cliqué, le transfert des photos a lieu

    :param source_folder:
    :param destination_folder:
    :return: TRUE ou FALSE

    """
    message = 'Vous confirmez les répertoires? \n' + \
              'Source : ' + source_folder + '\n' \
                                            'Destination : ' + destination_folder

    title = 'Confirmation'
    if ccbox(message, title):
        response = True
    else:
        response = False

    return response


def find_creation_date(filename):
    """
    retrouver la date de création d'un fichier

    :param filename: le nom complet du fichier (basestring)
    :return: la date de modification du fichier (date)

    """
    t = os.path.getctime(filename)
    return datetime.datetime.fromtimestamp(t).strftime('%Y_%m_%d')


def get_folder():
    """
    Retourne le chemin complet d'un répertoire choisi à l'écran

    :param direction:
    :return: le chemin complet du répertoire choisi à l'écran (source ou destination)
    """
    folders = {'source': '/volumes/photo/iphone', 'destination': '/volumes/photo'}
    folder = diropenbox()

    return folder
