import pygame
from pygame_menu import themes


# Couleurs
ROUGE = (205, 92, 92)
VERT = (0, 150, 0)
BLEU = (0, 0, 255)
CYAN = (0, 100, 100)
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)

SOLAIRE = themes.THEME_SOLARIZED
BLEUTE = themes.THEME_BLUE
LARGEUR, HAUTEUR = 700, 600
surface = pygame.display.set_mode ((LARGEUR, HAUTEUR))

# Fonction vide
def vide ():
    pass
