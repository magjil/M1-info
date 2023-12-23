from donnees import *



class Ecran:


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



    def ajouter (self, element, texte = "", action = vide, choix = list (), fond = BEIGE, police = NOIR):


        match (element):


            case "bouton":

                self.menu.add.button (
                    texte,
                    action,
                    font_color = police,
                    background_color = fond
                )


            case "zoneTexte":

                self.entreesConfiguration [texte] = self.menu.add.text_input (
                    texte + " : ",
                    default = "",
                    maxchar = 21
                )


            case "selecteur":

                self.entreesConfiguration [texte] = self.menu.add.selector (
                    texte + " : ",
                    choix,
                    onchange = action,
                    margin = (0, 30),
                    shadow_width = 15
                )


            case "levier":

                self.entreesConfiguration [texte] = self.menu.add.toggle_switch (
                    title = texte,
                    default = True,
                    margin = (0, 30),
                    shadow_width = 15
                )


            case other:

                print ("L'élément " + element + "n'est pas reconnu par l'interface.")
                exit (1)



    def enregistrer (self):
        
        # Lecture des valeurs dans les champs d'entrée
        configuration = {
            nom: entree.get_value ()
            for nom, entree in self.pere.entreesConfiguration.items ()
        }
        
        # Écriture dans un fichier Json
        nomFichier = self.entreesConfiguration ["Nom du fichier"].get_value ()
        ecrire (nomFichier, configuration)
        
        # Retour au menu précédent
        self.menu.reset (1)
