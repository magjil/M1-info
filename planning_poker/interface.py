from donnees import *



class Ecran:


    # Constructeur

    def __init__ (self, pere = None, titre = ""):


        # Test si l'écran est un sous-écran d'un autre

        self.pere = pere
        self.racine = pere == None


        # Création de l'écran

        if self.racine:
            leTheme = SOLAIRE
        else:
            leTheme = BLEUTE

        self.menu = pygame_menu.Menu (
            titre,
            LARGEUR,
            HAUTEUR,
            theme = leTheme
        )


        # Configuration

        self.joueurs = set ()
        self.deck = set ()
        self.entreesConfiguration = dict ()



    def mettreAjour (self):

        if self.menu.is_enabled ():
            self.menu.update (pygame.event.get ())
            self.menu.draw (SURFACE)

        pygame.display.update ()


    def ouvrir (self):

        if self.racine:
            print ("Pas besoin d'ouvrir le menu principal.")
            exit (1)

        self.pere.menu._open (self.menu)



    # Ajouter un élément à l'écran

    def ajouter (
        self,
        element,
        texte = "",
        action = vide,
        choix = list (),
        fond = BEIGE,
        police = NOIR,
        marge = 30,
        alignement = pygame_menu.locals.ALIGN_CENTER
    ):

        objetCree = None


        match (element):

            case "label":

                objetCree = self.menu.add.label (
                    texte,
                    font_color = police,
                    background_color = fond,
                    margin = (0, marge),
                    shadow_width = 15,
                    align = alignement
                )

        
            case "zoneTexte":

                objetCree = self.menu.add.text_input (
                    texte + " : ... ",
                    font_color = police,
                    background_color = fond,
                    default = "",
                    maxchar = 21,
                    margin = (0, marge),
                    shadow_width = 15
                )
                
                objetCree.set_onmouseover (self.illuminer (objetCree, fond))
                objetCree.set_onmouseleave (self.reAssombrir (objetCree, fond))
                
                self.entreesConfiguration [texte] = objetCree


            case "levier":

                objetCree = self.menu.add.toggle_switch (
                    title = texte,
                    font_color = police,
                    background_color = fond,
                    default = True,
                    margin = (0, marge),
                    shadow_width = 15
                )
                
                objetCree.set_onmouseover (self.illuminer (objetCree, fond))
                objetCree.set_onmouseleave (self.reAssombrir (objetCree, fond))
                
                self.entreesConfiguration [texte] = objetCree


            case "bouton":

                objetCree = self.menu.add.button (
                    texte,
                    action,
                    font_color = police,
                    background_color = fond,
                    margin = (0, marge),
                    shadow_width = 15
                )
                
                objetCree.set_onmouseover (self.illuminer (objetCree, fond))
                objetCree.set_onmouseleave (self.reAssombrir (objetCree, fond))


            case "selecteur":

                objetCree = self.menu.add.selector (
                    texte + " : ",
                    choix,
                    onchange = action,
                    font_color = police,
                    background_color = fond,
                    margin = (0, marge),
                    shadow_width = 15
                )
                
                objetCree.set_onmouseover (self.illuminer (objetCree, fond))
                objetCree.set_onmouseleave (self.reAssombrir (objetCree, fond))
                
                self.entreesConfiguration [texte] = objetCree
                
                
            case "space":

                objetCree = self.menu.add.label (
                    "",
                    font_color = police,
                    background_color = fond,
                    margin = (0, marge)
                )
                
            
            case "cadre":

                objetCree = self.menu.add._frame (
                    width = 117,
                    height = 181,
                    orientation = pygame_menu.locals.ORIENTATION_HORIZONTAL
                )
            
            
            case "image":

                objetCree = self.menu.add.image (
                    cheminImages + texte
                )


            case other:

                print ("L'élément " + element + "n'est pas reconnu par l'interface.")
                exit (1)
        
        
        return objetCree



    # Augmentation de la luminosité quand l'objet est sélectionné

    def illuminer (self, cible, fond):
    
        # Moyenne entre du blanc et la couleur d'origine
        fond = tuple (
            (couleur + 255) // 2
            for couleur in fond
        )
        
        def fonctionnelle ():
            cible.set_background_color (fond)
        
        return fonctionnelle
        
        
    def reAssombrir (self, cible, fond):
        
        # Remise de la couleur d'origine
        def fonctionnelle ():
            cible.set_background_color (fond)
        
        return fonctionnelle
        


    # Gestion des joueurs
    
    def ajouterJoueur (self):
    
        nomJoueur = self.obtenirConfig () ["Nom du joueur"]
        self.joueurs.add (nomJoueur)
    
    
    def supprimerJoueur (self):
    
        nomJoueur = self.obtenirConfig () ["Nom du joueur"]
        self.joueurs.discard (nomJoueur)



    # Gestion du deck
    
    def ajouterTache (self):
    
        nomTache = self.obtenirConfig () ["Nom de la tâche"]
        self.deck.add (nomTache)
    
    
    def supprimerTache (self):
    
        nomTache = self.obtenirConfig () ["Nom de la tâche"]
        self.deck.discard (nomTache)



    # Gestion de la configuration

    def obtenirConfig (self):

        # Lecture des valeurs dans les champs d'entrée
        configuration = {
            nom: entree.get_value ()
            for nom, entree in self.entreesConfiguration.items ()
        }
        
        # Récupération des joueurs
        configuration ["joueurs"] = list (self.joueurs)
        
        # Récupération du deck
        configuration ["deck"] = list (self.deck)

        return configuration


    def enregistrer (self):
        
        # Écriture dans un fichier Json
        nomFichier = self.entreesConfiguration ["Nom du fichier"].get_value ()
        ecrire (nomFichier, self.pere.obtenirConfig ())
        
        # Retour au menu précédent
        self.menu.reset (1)
