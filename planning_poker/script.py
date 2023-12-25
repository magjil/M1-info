"""
ce bout de code jsp à quoi il sert donc je l'ai gardé là :


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


from calculs import *
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

    global boutonLancer, boutonOuvrir
    boutonLancer = menuPrincipal.ajouter (
        element = "bouton",
        texte = "JOUER",
        action = lancer
    )
    boutonOuvrir = menuPrincipal.ajouter (
        element = "bouton",
        texte = "JOUER",
        action = enJeu.ouvrir
    )
    boutonOuvrir.hide ()

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


    # Pour ne pas lancer le jeu plusieurs fois

    boutonLancer.hide ()
    boutonOuvrir.show ()


    # Mise en place

    global config
    config = menuOptions.obtenirConfig ()

    ensJoueurs = {"John", "Harry", "Sherlock"}
    sommeVoix = [0]

    dicoTaches = {"pont": 0, "immeuble": 0}
    if dicoTaches == dict ():
        print ("Vous devez définir au moins une tâche dans le menu des options.")
        exit (1)

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

    aQuiLeTour = enJeu.ajouter (
        element = "label",
        texte = "",
        police = NOIR,
        fond = CYAN,
    )

    for tache in dicoTaches:
        enJeu.ajouter (
            element = "bouton",
            texte = tache,
            action = voix (sommeVoix, dicoTaches, tache)
        )
    
    enJeu.ouvrir ()


    # --- Décision de la tâche d'étalonnage (qui vaut 1) ---

    choisie = None
    premierPassage = True

    # L'on continue tant qu'aucune tâche n'a été élue
    while choisie == None:

        # Les joueurs votent chacun leur tour
        for joueur in ensJoueurs:
            sommeVoixActuelle = sommeVoix [0] 
            aQuiLeTour.set_title ("C'est à " + joueur + " de voter.")

            # Rafraîchissement de l'écran tant que le joueur n'a pas voté
            while sommeVoixActuelle == sommeVoix [0]:
                menuPrincipal.mettreAjour ()

        # Choix de la tâche par unanimité
        if premierPassage or config ["Mode de jeu"] == "Attendre l'unanimité":
            choisie = unanimite (dicoTaches)

            # L'unanimité n'a pas été atteinte
            premierPassage = False
        
        # Choix de la tâche par majorité relative
        else:
            choisie = majoriteRelative (dicoTaches)
            
        # L'on réinitialise les voix
        sommeVoix [0] = 0
        for tache in dicoTaches:
            dicoTaches [tache] = 0
    

    # Les priorites sont initialisées à None
    
    tachesRestantes = dicoTaches.keys () - {choisie}
    
    for tache in tachesRestantes:
        dicoTaches [tache] = None


    # Mise à jour du backlog

    dicoTaches [choisie] = 1
    enJeu.menu.clear ()
    afficher (dicoTaches)


    # Mise en place
    
    enJeu.ajouter (
        element = "label",
        texte = "Votez pour un coût de la tâche :",
        police = BLANC,
        fond = VERT,
        marge = 0
    )

    labelTache = enJeu.ajouter (
        element = "label",
        texte = "",
        police = BLANC,
        fond = VERT,
        marge = 30
    )
    
    aQuiLeTour = enJeu.ajouter (
        element = "label",
        texte = "",
        police = NOIR,
        fond = CYAN,
    )
    
    
    # --- Décision des coûts des tâches ---

    for tache in tachesRestantes:
        labelTache.set_title (tache)
        choisie = None
        
        # L'on continue tant qu'aucune tâche n'a été élue
        while choisie == None:
        
            # Les joueurs votent chacun leur tour
            for joueur in ensJoueurs:
                sommeVoixActuelle = sommeVoix [0] 
                aQuiLeTour.set_title ("C'est à " + joueur + " de voter.")
                
                # Rafraîchissement de l'écran tant que le joueur n'a pas voté
                while sommeVoixActuelle == sommeVoix [0]:
                    menuPrincipal.mettreAjour ()
                    
            # Choix de la tâche par unanimité
            if premierPassage or config ["Mode de jeu"] == "Attendre l'unanimité":
                choisie = unanimite (dicoTaches)

                # L'unanimité n'a pas été atteinte
                premierPassage = False
            
            # Choix de la tâche par majorité relative
            else:
                choisie = majoriteRelative (dicoTaches)
                
            # L'on réinitialise les voix
            sommeVoix [0] = 0
            
    # à faire : finir ça lul


def voix (sommeVoix, dicoTaches, tache):
    def fonctionnelle ():

        sommeVoix [0] += 1
        dicoTaches [tache] += 1

    return fonctionnelle


def afficher (backlog):

    # à faire : mettre le bakclog à gauche ou à droite

    enJeu.ajouter (
        element = "label",
        texte = "- Backlog -",
        police = BLANC,
        fond = MAGENTA,
    )

    for tache, cout in backlog.items ():
        if cout != None:
        
            enJeu.ajouter (
                element = "label",
                texte = tache + " : " + str (cout),
                police = BLANC,
                fond = MAGENTA,
                marge = 0
            )
    

# Le menu se met à jour tout seul si un autre objet est ajouté ou supprimé

def bouclePrincipale ():

    while True:
        menuPrincipal.mettreAjour ()


initialiser ()
bouclePrincipale ()
