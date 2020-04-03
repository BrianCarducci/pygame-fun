import pygame
from entities import player
pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Game")
pygame.init()

width = 40
height = 60
x = 250
y = SCREEN_HEIGHT - height
vel = 15

the_player = player.Player(x, y, width, height, vel, False, 10)
entities = [the_player]


def draw(entities):
    for entity in entities:
        win.fill((0, 0, 0))
        pygame.draw.rect(win, (255, 0, 0), (entity.x, entity.y, entity.width, entity.height))
        pygame.display.update()


run = True
while run:
    pygame.time.delay(25)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    the_player.check_player_actions(keys, "playing", SCREEN_WIDTH)
    draw(entities)

pygame.quit()