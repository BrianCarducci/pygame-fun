import os
import pygame

from entities.player import Player
from entities.environment.platform import Platform
from state import State



def setup(window_width, window_height):
    width = window_width/18
    height = window_height/14
    # x = 250
    y = window_height - height
    vel = 15
    game_state = State.PLAYING
    # set up background
    bg = pygame.image.load(os.path.join("assets", "backgrounds" ,"bg.png")).convert()

    # set up font
    font = pygame.font.Font(pygame.font.get_default_font(), 25)

    # set up environment
    # floor = Platform(700, y, width, height, 0, (0, 255, 0), 1200)
    floor = Platform(pygame.Rect(700, y, width, height), 0, (0, 255, 0), 700)

    # set up NPCs

    # initialize array of all entities, which will be iterated through and drawn each game loop tick
    entities = [floor]

    #set up player
    # player = Player(window_width//2, y, width, height, vel, (255, 0, 0), entities, window_width//2, False, 10)
    player = Player(pygame.Rect(window_width//2, y, width, height), vel, (255, 0, 0), window_width//2, False, 10)

    return game_state, font, bg, player, entities