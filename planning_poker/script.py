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
        texte = "LANCER",
        action = lancer,
        police = MAGENTA
    )
    boutonOuvrir = menuPrincipal.ajouter (
        element = "bouton",
        texte = "LANCER",
        action = enJeu.ouvrir,
        police = MAGENTA
    )
    boutonOuvrir.hide ()

    boutonOptions = menuPrincipal.ajouter (
        element = "bouton",
        texte = "OPTIONS",
        action = menuOptions.ouvrir,
        police = BLEU
    )

    boutonQuitter = menuPrincipal.ajouter (
        element = "bouton",
        texte = "QUITTER",
        action = pygame_menu.events.EXIT
    )
    
    boutonLancer.scale (2, 2)
    boutonOuvrir.scale (2, 2)
    boutonOptions.scale (2, 2)
    boutonQuitter.scale (2, 2)


    # Menu des options

    menuOptions.ajouter (
        element = "levier",
        texte = "Musique",
        fond = TURQUOISE,
        marge = 0
    )

    menuOptions.ajouter (
        element = "levier",
        texte = "Effets sonores",
        fond = TURQUOISE
    )
    
    menuOptions.ajouter (
        element = "zoneTexte",
        texte = "Temps du tour en s.",
        fond = CYAN,
        marge = 0
    )

    menuOptions.ajouter (
        element = "selecteur",
        texte = "Mode de jeu",
        choix = modesJeu [:],
        fond = CYAN
    )
    
    menuOptions.ajouter (
        element = "zoneTexte",
        texte = "Nom du joueur",
        police = BLANC,
        fond = MAGENTA,
        marge = 0
    )
    
    menuOptions.ajouter (
        element = "bouton",
        texte = "Ajouter",
        action = menuOptions.ajouterJoueur,
        police = BLANC,
        fond = MAGENTA,
        marge = 0
    )
    
    menuOptions.ajouter (
        element = "bouton",
        texte = "Supprimer",
        action = menuOptions.supprimerJoueur,
        police = BLANC,
        fond = MAGENTA
    )
    
    menuOptions.ajouter (
        element = "zoneTexte",
        texte = "Nom de la tâche",
        police = BLANC,
        fond = BLEU,
        marge = 0
    )
    
    menuOptions.ajouter (
        element = "bouton",
        texte = "Ajouter",
        action = menuOptions.ajouterTache,
        police = BLANC,
        fond = BLEU,
        marge = 0
    )
    
    menuOptions.ajouter (
        element = "bouton",
        texte = "Supprimer",
        action = menuOptions.supprimerTache,
        police = BLANC,
        fond = BLEU
    )

    # Scan des configurations sauvegardées
    preselections = [("Sélection actuelle", "")]
    for configSauvegardee in os.listdir (cheminConfigs + "/"):

        # Gestion du format
        if configSauvegardee[-5:] == ".json":
            configSauvegardee = configSauvegardee[: -5]
            preselections.append ((configSauvegardee, ""))

    menuOptions.ajouter (
        element = "listeDeroulante",
        texte = "Configuration",
        choix = preselections,
        description = "Présélection des options"
    )

    menuOptions.ajouter (
        element = "bouton",
        texte = "Enregistrer-sous",
        action = menuEnregistrement.ouvrir,
        fond = VERT,
        police = BLANC,
        marge = 0
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

    ensJoueurs = config ["joueurs"]
    sommeVoix = [0]

    dicoTaches = {
        tache: 0
        for tache in config ["deck"]
    }
    if dicoTaches == dict ():
        print ("Vous devez définir au moins une tâche dans le menu des options.")
        exit (1)

    enJeu.ajouter (
        element = "label",
        texte = "Votez pour une tache d'étalonnage",
        marge = 0
    )

    enJeu.ajouter (
        element = "label",
        texte = "qui aura 1 comme priorité :"
    )

    aQuiLeTour = enJeu.ajouter (
        element = "label",
        texte = "",
        police = BLANC,
        fond = MAGENTA,
    )

    for tache in dicoTaches:
        enJeu.ajouter (
            element = "bouton",
            texte = tache,
            action = voix (sommeVoix, dicoTaches, tache),
            fond = TURQUOISE,
            marge = 0
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
        marge = 0
    )

    labelTache = enJeu.ajouter (
        element = "label",
        texte = "",
        fond = VERT,
        marge = 30
    )
    
    aQuiLeTour = enJeu.ajouter (
        element = "label",
        texte = "",
        police = BLANC,
        fond = MAGENTA,
    )
    
    for nomCarte in nomCartes:
        enJeu.ajouter ("image", "cartes_" + nomCarte + ".png")       
    
    
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
            
    


def voix (sommeVoix, dicoTaches, tache):
    def fonctionnelle ():

        sommeVoix [0] += 1
        dicoTaches [tache] += 1

    return fonctionnelle


def afficher (backlog):

    enJeu.ajouter (
        element = "label",
        texte = "- Backlog -",
        police = BLANC,
        fond = BLEU,
        alignement = pygame_menu.locals.ALIGN_LEFT
    )

    for tache, cout in backlog.items ():
        if cout != None:
        
            enJeu.ajouter (
                element = "label",
                texte = tache + " : " + str (cout),
                police = BLANC,
                fond = BLEU,
                marge = 0,
                alignement = pygame_menu.locals.ALIGN_LEFT
            )
            
    enJeu.ajouter (
        element = "space",
        police = BLANC,
        fond = TURQUOISE,
        marge = 0
    )
    

# Le menu se met à jour tout seul si un autre objet est ajouté ou supprimé

def bouclePrincipale ():

    while True:
        menuPrincipal.mettreAjour ()


initialiser ()
bouclePrincipale ()
