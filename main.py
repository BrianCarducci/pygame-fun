import os
import pygame
import pyautogui
import setup

from state import State
from entities.player import Player


def main():
    pygame.init()

    # myFont = pygame.font.SysFont("Comic Sans MS", 30)

    # GAME_FONT = pygame.freetype.Font("", 24)

    # os.environ['SDL_VIDEO_WINDOW_POS'] = str(0) + "," + str(20)

    GAME_FONT = pygame.font.Font(pygame.font.get_default_font(), 25)

    # WINDOW_WIDTH = 500
    # WINDOW_HEIGHT = 500
    WINDOW_WIDTH, WINDOW_HEIGHT = pyautogui.size()

    game_state = State.PLAYING

    win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("My Game")
    pygame.init()

    width = WINDOW_WIDTH/18
    height = WINDOW_HEIGHT/14
    x = 250
    y = WINDOW_HEIGHT - height
    vel = 15

    player = Player(x, y, width, height, vel, False, 10)
    entities = [player]

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
            if event.type == pygame.VIDEORESIZE:
                WINDOW_WIDTH = event.w
                WINDOW_HEIGHT = event.h
                print("resize event: " + str(WINDOW_WIDTH) + ", " + str(WINDOW_HEIGHT))
                
        keys = pygame.key.get_pressed()

        player.check_player_actions(keys, game_state, WINDOW_WIDTH)
        draw(entities, text_surface, win, WINDOW_WIDTH, WINDOW_HEIGHT)

    pygame.quit()


def draw(entities, text_surface, win, window_width, window_height):
    for entity in entities:
        win.fill((0, 0, 0))
        pygame.draw.rect(win, (255, 0, 0), (entity.x, entity.y, entity.width, entity.height))

    if text_surface:
        w, h = pygame.display.get_surface().get_size()
        print("from get surface: " + str(win.get_width()) + ", " + str(win.get_height()))
        win.blit(text_surface, (window_width/2, window_height/2))

    pygame.display.update()


if __name__ == "__main__":
    main()

