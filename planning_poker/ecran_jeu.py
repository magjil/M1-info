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


# ---------------------------------------------------

    global mainmenu, Options
    entreesConfiguration = dict ()
    

    
    # Menu principal
    mainmenu = pygame_menu.Menu('PLANNING POKER', LARGEUR, HAUTEUR)
    mainmenu.add.button('JOUER', start_the_game)
    mainmenu.add.button('OPTIONS', Options_menu)
    mainmenu.add.button('QUITTER', )

    # Menu des options
    Options = pygame_menu.Menu('Menu des options', LARGEUR, HAUTEUR)
    
    entreesConfiguration ["difficulte"] = Options.add.selector('Difficulté : ', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty, margin=(0, 30),
            shadow_width=15)
    entreesConfiguration ["musique"] = Options.add.toggle_switch(title="Musique", default=True, margin=(0, 30),
            shadow_width=15)
    entreesConfiguration ["sons"] = Options.add.toggle_switch(title="Sons", default=True,margin=(0, 30),
            shadow_width=15)
    Options.add.button (title = "Enregistrer-sous", action = enregistrerSous, font_color = BLANC, background_color = VERT, margin=(0, 30),
            shadow_width=15,)
    Options.add.button (title = "Réinitialiser", action = Options.reset_value, font_color = BLANC, background_color=(205, 92, 92), margin=(0, 30),
            shadow_width=15)

    
    # Menu d'enregistrement
    menuEnregistrement = pygame_menu.Menu("Sauvegarder la configuration...", LARGEUR, HAUTEUR)
    
    menuEnregistrement.add.button ('Valider', enregistrer (entreesConfiguration))


def set_difficulty(value, difficulty):
    print(value)
    print(difficulty)
 
def start_the_game ():
    pass
    
def Options_menu ():
    mainmenu._open (Options)
    
def enregistrerSous ():
    Options._open (menuEnregistrement)



def enregistrer (entreesConfiguration):
    def fonctionnelle ():
    
        # Lecture des valeurs dans les champs d'entrée
        configuration = {
            nom: entree.get_value ()
            for nom, entree in entreesConfiguration.items ()
        }
        
        # Écriture dans un fichier Json
        nomFichier = configuration ["nomFichier"]
        ecrire (nomFichier, configuration)
        
        # Retour au menu des options
        menuEnregistrement.reset (1)
        
        
    return fonctionnelle








    
    

    



# Le menu se met à jour tout seul si un autre objet est ajouté ou supprimé

def bouclePrincipale ():

    while True:
        menuPrincipal.mettreAjour ()


initialisation ()
bouclePrincipale ()
