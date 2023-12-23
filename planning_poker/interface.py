import pygame
import pygame_menu

from constantes import *
from donnees import *



class Ecran:


    def __init__ (self, father = None, titre = ""):


        # Test si l'écran est un sous-écran d'un autre

        self.father = father
        self.racine = father == None


        # Création de l'écran

        if self.racine:
            leTheme = SOLAIRE
        else:
            leTheme = BLEUTE

        self.ecran = pygame_menu.Menu (
            titre,
            LARGEUR,
            HAUTEUR,
            theme = leTheme
        )


        # Configuration

        self.entreesConfiguration = dict ()



    def ouvrir (self):


        if self.racine:
            print ("Pas besoin d'ouvrir le menu principal.")
            exit (1)

        self.father._open (self.ecran)



    def ajouter (self, element, texte = "", action = vide, choix = list ()):


        match (element):


            case "bouton":

                self.ecran.add.button (texte, action)


            case "zoneTexte":

                entreesConfiguration [texte] = menuEnregistrement.add.text_input (
                    texte + " : ",
                    default = "",
                    maxchar = 21
                )


            case "selecteur":

                self.entreesConfiguration [texte] = self.ecran.add.selector (
                    texte + " : ",
                    choix,
                    onchange = action,
                    margin = (0, 30),
                    shadow_width = 15
                )


            case "levier":

                self.entreesConfiguration [texte] = Options.add.toggle_switch (
                    title = texte,
                    default = True,
                    margin = (0, 30),
                    shadow_width = 15
                )


            case other:

                print ("L'élément " + element + "n'est pas reconnu par l'interface.")
                exit (1)



    def enregistrer (self):
        def fonctionnelle ():
        
            # Lecture des valeurs dans les champs d'entrée
            configuration = {
                nom: entree.get_value ()
                for nom, entree in self.entreesConfiguration.items ()
            }
            
            # Écriture dans un fichier Json
            nomFichier = configuration ["Nom"]
            ecrire (nomFichier, configuration)
            
            # Retour au menu précédent
            self.ecran.reset (1)
            
            
        return fonctionnelle
