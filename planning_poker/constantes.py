import json
import os
import pygame
import pygame_menu
from pathlib import Path


# Données
cheminDonnees = str (Path (__file__).resolve ().parent) + "/donnees"

# Couleurs
ROUGE   = (150, 0  , 0  )
VERT    = (0  , 150, 0  )
BLEU    = (0  , 0  , 150)
CYAN    = (0  , 200, 200)
MAGENTA = (200, 0  , 200)
JAUNE   = (200, 200, 0  )
BEIGE   = (239, 231, 211)
NOIR    = (0  , 0  , 0  )
BLANC   = (255, 255, 255)

# Disposition
SOLAIRE = pygame_menu.themes.THEME_SOLARIZED
BLEUTE = pygame_menu.themes.THEME_BLUE
LARGEUR, HAUTEUR = 700, 600
SURFACE = pygame.display.set_mode ((LARGEUR, HAUTEUR))

# Modes de jeu
modesJeu = list ()
modesJeu.append (("Majorité relative", None))
modesJeu.append (("Médiane", None))
modesJeu.append (("Moyenne", None))
modesJeu.append (("Attendre l'unanimité", None))

# Fonction vide
def vide (arg1 = None, arg2 = None):
    pass
