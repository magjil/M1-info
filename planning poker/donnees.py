import json
import os
from pathlib import Path


global cheminDonnees
cheminDonnees = str (Path (__file__).resolve ().parent) + "/donnees"


def ecrire (nomFichier, donnees):

    chemin = cheminDonnees + "/" + nomFichier + ".json"
    fichier = open (chemin, "w")
    json.dump (donnees, fichier, indent = 4)


def lire (nomFichier):

    chemin = cheminDonnees + nomFichier + ".json"
    fichier = open (chemin, "r")
    return json.load (fichier)


def main ():

    if not os.path.isdir (cheminDonnees):
        os.mkdir (cheminDonnees)


main ()
