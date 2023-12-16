# rebonjour
from tkinter import *
import pygame, sys
from time import sleep
import pygame_menu as pm
from pygame_menu import themes



pygame.init()
pygame.display.set_caption('PLANNING POKER')
screen = pygame.display.set_mode((500, 500),0,32)
 
from time import sleep
import pygame
import pygame_menu
from pygame_menu import themes
 
pygame.init()

WIDTH, HEIGHT = 700,600
RED = (255, 0, 0) 
GREEN = (0, 255, 0) 
BLUE = (0, 0, 255) 
CYAN = (0, 100, 100) 
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255)
surface = pygame.display.set_mode((WIDTH,HEIGHT))
 
def set_difficulty(value, difficulty):
    print(value)
    print(difficulty)
 
def start_the_game():
    mainmenu._open(principale_screen)

def Options_menu():
    mainmenu._open(Options)
    
    
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
  
 
mainmenu = pygame_menu.Menu('PLANNING POKER', WIDTH, HEIGHT, theme=themes.THEME_SOLARIZED)

mainmenu.add.button('JOUER', start_the_game)
mainmenu.add.button('OPTIONS', Options_menu)
mainmenu.add.button('QUITTER', pygame_menu.events.EXIT)

principale_screen = pygame_menu.Menu("Menu d'enregistrement", WIDTH, HEIGHT, theme=themes.THEME_BLUE)
Options = pm.Menu('Menu des options', WIDTH, HEIGHT, theme=themes.THEME_BLUE)
Options.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
principale_screen.add.text_input('Nom :', default= 'username', maxchar=20 )
#Options.add.dropselect(title="", items = , dropselect_id="Choix du deck", default=0)
#Options.add.dropselect(title="Graphics Level", items=graphics, dropselect_id="graphics level", default=0) 
Options.add.toggle_switch(title="Music", default=True, toggleswitch_id="music") 
Options.add.toggle_switch(title="Sounds", default=False, toggleswitch_id="sound") 
Options.add.button(title="Restore Defaults", action=Options.reset_value, 
                        font_color=WHITE, background_color=RED) 
Options.add.resolution = []

mainmenu._theme.widget_alignment = pm.locals.ALIGN_CENTER 

mainmenu.mainloop(surface)
