from constantes import *


def ecrire (nomFichier, donnees):

    chemin = cheminConfigs + "/" + nomFichier + ".json"
    fichier = open (chemin, "w")
    json.dump (donnees, fichier, indent = 4)


def lire (nomFichier):

    chemin = cheminConfigs + "/" + nomFichier + ".json"
    fichier = open (chemin, "r")
    return json.load (fichier)


def dossierDonnees ():

    if not os.path.isdir (cheminConfigs):
        os.mkdir (cheminConfigs)


dossierDonnees ()
