import os
import pygame

from entities.player import Player


def setup(window_width, window_height):
    # set up background
    bg = pygame.image.load(os.path.join("assets", "backgrounds" ,"bg.png")).convert()

    # set up font
    font = pygame.font.Font(pygame.font.get_default_font(), 25)

    #set up player
    width = window_width/18
    height = window_height/14
    # x = 250
    y = window_height - height
    vel = 15
    player = Player(window_width//2, y, width, height, vel, window_width//2, False, 10)

    # set up environment

    # set up NPCs

    # initialize array of all entities, which will be iterated through and drawn each game loop tick
    entities = [player]

    return font, bg, entities