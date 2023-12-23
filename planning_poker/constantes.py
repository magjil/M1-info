import json
import os
import pygame
import pygame_menu
from pathlib import Path


# Données
cheminDonnees = str (Path (__file__).resolve ().parent) + "/donnees"

# Couleurs
ROUGE = (205, 92,  92 )
VERT  = (0,   150, 0  )
BLEU  = (0,   0,   255)
CYAN  = (0,   100, 100)
NOIR  = (0,   0,   0  )
BLANC = (255, 255, 255)

# Disposition
SOLAIRE = pygame_menu.themes.THEME_SOLARIZED
BLEUTE = pygame_menu.themes.THEME_BLUE
LARGEUR, HAUTEUR = 700, 600
SURFACE = pygame.display.set_mode ((LARGEUR, HAUTEUR))

# Modes de jeu
modesJeu = list ()
modesJeu.append (("Majorité absolue", None))
modesJeu.append (("Majorité relative", None))
modesJeu.append (("Médiane", None))
modesJeu.append (("Moyenne", None))
modesJeu.append (("Attendre l'unanimité", None))

# Fonction vide
def vide (arg1 = None, arg2 = None):
    pass
