import os
import pygame
import pyautogui

from setup import setup
from state import State
from entities.player import Player


def main():
    pygame.init()

    os.environ['SDL_VIDEO_WINDOW_POS'] = str(0) + "," + str(20)

    # GAME_FONT = pygame.font.Font(pygame.font.get_default_font(), 25)
    # WINDOW_WIDTH, WINDOW_HEIGHT = pyautogui.size()
    # WINDOW_WIDTH, WINDOW_HEIGHT = 800, 447
    # WINDOW_WIDTH, WINDOW_HEIGHT = 1920, 1080
    WINDOW_WIDTH, WINDOW_HEIGHT = 2560, 1440
    win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    game_state, GAME_FONT, background, player, entities = setup(WINDOW_WIDTH, WINDOW_HEIGHT)
    background_x = 0
    background_x2 = background.get_width()

    pygame.display.set_caption("My Game")
    pygame.init()

    # player = entities[0]
    text_surface = None

    run = True
    while run:
        pygame.time.delay(25)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if game_state == State.PLAYING:
                        game_state = State.PAUSED
                        text_surface = GAME_FONT.render("Paused", True, (255, 0, 0))
                    elif game_state == State.PAUSED:
                        game_state = State.PLAYING
                        text_surface = None
                if event.key == pygame.K_ESCAPE:
                    if WINDOW_WIDTH == 2560:
                        WINDOW_WIDTH, WINDOW_HEIGHT = 1920, 1080
                        win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
                    else:
                        WINDOW_WIDTH, WINDOW_HEIGHT = 2560, 1440
                        win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
            # if event.type == pygame.VIDEORESIZE:
            #     WINDOW_WIDTH = event.w
            #     WINDOW_HEIGHT = event.h
                
        keys = pygame.key.get_pressed()

        player.check_player_collisions(entities)
        if player.is_dead(WINDOW_HEIGHT):
            game_state, GAME_FONT, background, player, entities = setup(WINDOW_WIDTH, WINDOW_HEIGHT)

        background_x, background_x2 = player.check_player_actions(entities, keys, game_state, WINDOW_WIDTH, background_x, background_x2)

        if background_x < background.get_width() * -1:
            background_x = background.get_width()

        if background_x2 < background.get_width() * -1:
            background_x2 = background.get_width()

        draw(player, entities, background, text_surface, win, WINDOW_WIDTH, WINDOW_HEIGHT, background_x, background_x2)

    pygame.quit()


def draw(player, entities, background, text_surface, win, window_width, window_height, background_x, background_x2):
    win.fill((0, 0, 0))

    win.blit(background, (background_x, 0))
    win.blit(background, (background_x2, 0))

    pygame.draw.rect(win, player.sprite, player.hitbox)

    for entity in entities:
        # win.blit(background, (background_x, 0))
        # win.blit(background, (background_x2, 0))
        pygame.draw.rect(win, entity.sprite, entity.hitbox)

    if text_surface:
        w, h = pygame.display.get_surface().get_size()
        print("from get surface: " + str(win.get_width()) + ", " + str(win.get_height()))
        win.blit(text_surface, (window_width//2, window_height//2))

    pygame.display.update()


if __name__ == "__main__":
    main()

