import pygame; from pygame import mixer; pygame.init(); import colorama; from colorama import Fore; colorama.init()

def new_ability(ability= str):

    if ability == "conocimientos-ragano":

        path = "./Assets/Music/ability.mp3"

        pygame.mixer.init()
        pygame.mixer.Sound(path).play()




