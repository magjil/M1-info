import json
import os

from constantes import *


def ecrire (nomFichier, donnees):

    chemin = cheminDonnees + "/" + nomFichier + ".json"
    fichier = open (chemin, "w")
    json.dump (donnees, fichier, indent = 4)


def lire (nomFichier):

    chemin = cheminDonnees + nomFichier + ".json"
    fichier = open (chemin, "r")
    return json.load (fichier)


def dossierDonnees ():

    if not os.path.isdir (cheminDonnees):
        os.mkdir (cheminDonnees)


dossierDonnees ()
