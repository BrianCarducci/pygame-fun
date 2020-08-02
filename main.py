import pygame
import pygame.freetype
import setup

from state import State
from entities.player import Player

def main():
    pygame.init()

    # myFont = pygame.font.SysFont("Comic Sans MS", 30)

    # GAME_FONT = pygame.freetype.Font("", 24)

    GAME_FONT = pygame.font.Font(pygame.font.get_default_font(), 25)

    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 500

    game_state = State.PLAYING


    win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("My Game")
    pygame.init()

    width = 40
    height = 60
    x = 250
    y = SCREEN_HEIGHT - height
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if game_state == State.PLAYING:
                        game_state = State.PAUSED
                        text_surface = GAME_FONT.render("Paused", True, (255, 0, 0))
                    elif game_state == State.PAUSED:
                        game_state = State.PLAYING
                        text_surface = None
        
        keys = pygame.key.get_pressed()

        player.check_player_actions(keys, game_state, SCREEN_WIDTH)
        draw(entities, text_surface, win)

    pygame.quit()


def draw(entities, text_surface, win):
    for entity in entities:
        win.fill((0, 0, 0))
        pygame.draw.rect(win, (255, 0, 0), (entity.x, entity.y, entity.width, entity.height))

    if text_surface:
        win.blit(text_surface, (250, 250))

    pygame.display.update()


if __name__ == "__main__":
    main()

