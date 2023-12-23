"""
from time import sleep
mainmenu._theme.widget_alignment = pygame_menu.locals.ALIGN_CENTER

def main(): 

    graphics = [("Low", "low"),
                ("Medium", "medium"),
                ("High", "high"),
                ("Ultra High", "ultra high")]

    resolution = [("1920x1080", "1920x1080"),
                  ("1920x1200", "1920x1200"),
                  ("1280x720", "1280x720"),
                  ("2560x1440", "2560x1440"),
                  ("3840x2160", "3840x2160")]

Options.add.dropselect(title="", items = , dropselect_id="Choix du deck", default=0)
Options.add.dropselect(title="Graphics Level", items=graphics, dropselect_id="graphics level", default=0)
"""


from interface import *



def initialisation ():


    # Fenêtre

    pygame.init ()
    pygame.display.set_caption ("PLANNING POKER")
    screen = pygame.display.set_mode ((LARGEUR, HAUTEUR), 0, 32)
    

    # Menus

    global menuPrincipal, menuOptions, menuEnregistrement

    menuPrincipal = Ecran (
        titre = "PLANNING POKER"
    )

    menuOptions = Ecran (
        titre = "Menu des options",
        pere = menuPrincipal
    )

    menuEnregistrement = Ecran (
        titre = "Sauvegarder la configuration...",
        pere = menuOptions
    )


    # Menu principal

    menuPrincipal.ajouter (
        element = "bouton",
        texte = "JOUER"
    )

    menuPrincipal.ajouter (
        element = "bouton",
        texte = "OPTIONS",
        action = menuOptions.ouvrir
    )

    menuPrincipal.ajouter (
        element = "bouton",
        texte = "QUITTER",
        action = pygame_menu.events.EXIT
    )


    # Menu des options

    menuOptions.ajouter (
        element = "levier",
        texte = "Musique",
    )

    menuOptions.ajouter (
        element = "levier",
        texte = "Effets sonores",
    )

    menuOptions.ajouter (
        element = "selecteur",
        texte = "Mode de jeu",
        choix = modesJeu [:]
    )

    menuOptions.ajouter (
        element = "bouton",
        texte = "Enregistrer-sous",
        action = menuEnregistrement.ouvrir,
        fond = BLEU,
        police = BLANC
    )

    menuOptions.ajouter (
        element = "bouton",
        texte = "Réinitialiser",
        action = menuOptions.menu.reset_value,
        fond = ROUGE,
        police = BLANC
    )


    # Menu d'enregistrement
    
    menuEnregistrement.ajouter (
        element = "zoneTexte",
        texte = "Nom du fichier"
    )

    menuEnregistrement.ajouter (
        element = "bouton",
        texte = "Valider",
        action = menuEnregistrement.enregistrer
    )



# Le menu se met à jour tout seul si un autre objet est ajouté ou supprimé

def bouclePrincipale ():

    while True:
        menuPrincipal.mettreAjour ()



initialisation ()
bouclePrincipale ()
