import os
import pygame

from entities.player import Player
from entities.environment.platform import Platform
from state import State



def setup(window_width, window_height):
    width = window_width/18
    height = window_height/14
    # x = 250
    floor_y = window_height - height
    vel = 15
    game_state = State.PLAYING
    # set up background
    bg = pygame.image.load(os.path.join("assets", "backgrounds" ,"bg.png")).convert()

    # set up font
    font = pygame.font.Font(pygame.font.get_default_font(), 25)

    # set up environment
    # floor = Platform(700, y, width, height, 0, (0, 255, 0), 1200)
    floor_1 = Platform(pygame.Rect(0, floor_y, 1000, height), 0, (0, 255, 0), 700)
    floor_2 = Platform(pygame.Rect(1200, floor_y, 1000, height), 0, (0, 255, 0), 700)
    ledge = Platform(pygame.Rect(700, floor_y - height, 200, height), 0, (0, 0, 255), 700)

    # set up NPCs

    # initialize array of all entities, which will be iterated through and drawn each game loop tick
    entities = [floor_1, ledge, floor_2]

    #set up player
    # player = Player(window_width//2, y, width, height, vel, (255, 0, 0), entities, window_width//2, False, 10)
    player = Player(pygame.Rect(window_width//2, floor_y - height - 200, width, height), vel, (255, 0, 0), window_width//2, False, 10)

    return game_state, font, bg, player, entities


def change_resolution(curr_window_width, new_window_width, curr_window_height, new_window_height, entities, player):
    scalar_x = new_window_width / curr_window_width
    scalar_y = new_window_height / curr_window_height

    scaled_entities = [_scale_entity(entity, scalar_x, scalar_y) for entity in entities]

    scaled_player = Player(pygame.Rect(player.hitbox.x*scalar_x, player.hitbox.y*scalar_y, player.hitbox.w*scalar_x, player.hitbox.h*scalar_y), player.vel*scalar_x, player.sprite, player.stage_location*scalar_x, player.is_jumping, player.jump_count)

    return new_window_width, new_window_height, scaled_entities, scaled_player


def _scale_entity(entity, scalar_x, scalar_y):
    entity.hitbox = pygame.Rect(
        entity.hitbox.x * scalar_x,
        entity.hitbox.y * scalar_y,
        entity.hitbox.w * scalar_x,
        entity.hitbox.h * scalar_y
    )
    entity.vel *= scalar_x
    return entity
