# from time import sleep

from donnees import *
from interface import *


pygame.init()
pygame.display.set_caption('PLANNING POKER')
screen = pygame.display.set_mode((500, 500),0,32)




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



def initialisation ():

    global mainmenu, menuEnregistrement, Options
    entreesConfiguration = dict ()

    # Menu principal
    mainmenu = pygame_menu.Menu('PLANNING POKER', WIDTH, HEIGHT, theme=themes.THEME_SOLARIZED)
    mainmenu.add.button('JOUER', start_the_game)
    mainmenu.add.button('OPTIONS', Options_menu)
    mainmenu.add.button('QUITTER', pygame_menu.events.EXIT)

    # Menu des options
    Options = pygame_menu.Menu('Menu des options', WIDTH, HEIGHT, theme=themes.THEME_BLUE)
    #Options.add.dropselect(title="", items = , dropselect_id="Choix du deck", default=0)
    #Options.add.dropselect(title="Graphics Level", items=graphics, dropselect_id="graphics level", default=0)
    entreesConfiguration ["difficulte"] = Options.add.selector('Difficulté : ', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty, margin=(0, 30),
            shadow_width=15)
    entreesConfiguration ["musique"] = Options.add.toggle_switch(title="Musique", default=True, toggleswitch_id="music", margin=(0, 30),
            shadow_width=15)
    entreesConfiguration ["sons"] = Options.add.toggle_switch(title="Sons", default=False, toggleswitch_id="sound",margin=(0, 30),
            shadow_width=15)
    Options.add.button (title = "Enregistrer-sous", action = enregistrerSous, font_color = WHITE, background_color = GREEN, margin=(0, 30),
            shadow_width=15,)
    Options.add.button (title = "Réinitialiser", action = Options.reset_value, font_color = WHITE, background_color=(205, 92, 92), margin=(0, 30),
            shadow_width=15)
    Options.add.resolution = []
    
    # Menu d'enregistrement
    menuEnregistrement = pygame_menu.Menu("Sauvegarder la configuration...", WIDTH, HEIGHT, theme=themes.THEME_BLUE)
    entreesConfiguration ["nomFichier"] = menuEnregistrement.add.text_input ("Nom : ", default = "", maxchar = 21)
    menuEnregistrement.add.button ('Valider', enregistrer (entreesConfiguration))
    
    

    mainmenu._theme.widget_alignment = pygame_menu.locals.ALIGN_CENTER



# Le menu se met à jour tout seul si un autre objet est ajouté ou supprimé

def bouclePrincipale ():

    while True:

        if mainmenu.is_enabled ():
            mainmenu.update (pygame.event.get ())
            mainmenu.draw (surface)
        pygame.display.update ()



initialisation ()
bouclePrincipale ()