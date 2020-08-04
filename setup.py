import os
import pygame

def setup():
    bg = pygame.image.load(os.path.join("assets", "backgrounds" ,"bg.png")).convert()
    font = pygame.font.Font(pygame.font.get_default_font(), 25)
    return font, bg