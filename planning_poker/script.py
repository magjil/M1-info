"""

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



# Création des objets

def initialiser ():


    # Fenêtre

    pygame.init ()
    pygame.display.set_caption ("PLANNING POKER")
    screen = pygame.display.set_mode ((LARGEUR, HAUTEUR), 0, 32)
    

    # Menus

    global menuPrincipal, enJeu, menuOptions, menuEnregistrement

    menuPrincipal = Ecran (
        titre = "Menu principal"
    )

    enJeu = Ecran (
        titre = "Planning",
        pere = menuPrincipal
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
        texte = "JOUER",
        action = lancer
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



# Lancement du jeu

def lancer ():


    # Mise en place

    global config
    config = menuOptions.obtenirConfig ()

    ensJoueurs = {"John", "Harry", "Sherlock"}
    sommeVoix = [0]
    dicoTaches = {"pont": 0, "immeuble": 0}

    enJeu.ouvrir ()


    aQuiLeTour = enJeu.ajouter (
        element = "label",
        texte = "",
        police = NOIR,
        fond = CYAN,
    )

    enJeu.ajouter (
        element = "label",
        texte = "Votez pour une tache d'étalonnage",
        police = BLANC,
        fond = VERT,
        marge = 0
    )

    enJeu.ajouter (
        element = "label",
        texte = "qui aura 1 comme priorité :",
        police = BLANC,
        fond = VERT,
        marge = 30
    )

    for tache in dicoTaches:
        enJeu.ajouter (
            element = "bouton",
            texte = tache,
            action = voix (sommeVoix, dicoTaches, tache)
        )


    # Décision de la tâche d'étalonnage (qui vaut 1)

    for joueur in ensJoueurs:
        sommeVoixActuelle = sommeVoix [0] 
        aQuiLeTour.set_title ("C'est à " + joueur + " de voter.")

        while sommeVoixActuelle == sommeVoix [0]:
            menuPrincipal.mettreAjour ()


def voix (sommeVoix, dicoTaches, tache):
    def fonctionnelle ():

        sommeVoix [0] += 1
        dicoTaches [tache] += 1

    return fonctionnelle


# Le menu se met à jour tout seul si un autre objet est ajouté ou supprimé

def bouclePrincipale ():

    while True:
        menuPrincipal.mettreAjour ()


initialiser ()
bouclePrincipale ()
