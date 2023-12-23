import pygame
import pygame_menu

from constantes import *


class Ecran:


    def __init__ (self, father = None, titre = ""):

        # Test si l'écran est un sous-écran d'un autre
        self.father = father
        self.racine = father == None

        # Création de l'écran
        if self.racine:
            leTheme = SOLAIRE
        else:
            leTheme = BLEUTE
        self.ecran = pygame_menu.Menu (titre, LARGEUR, HAUTEUR, theme = leTheme)

        # Configuration
        self.entreesConfiguration = dict ()


    def ouvrir (self):

        if self.racine:
            print ("Pas besoin d'ouvrir le menu principal.")
            exit (1)

        self.father._open (self.ecran)


    def ajouter (self, element, texte = "", action = vide):

        match (element):

            case "bouton":
                self.ecran.add.button (texte, action)



