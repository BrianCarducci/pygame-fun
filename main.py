import pygame
# from entities import *
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

is_jump = False
jump_count = 10
jump_coeff = -1

entities = Player()

# def draw(entities):
#     for entity in entities:
#         win.fill((0, 0, 0))
#         pygame.draw.


run = True
while run:
    pygame.time.delay(25)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        if x > vel:
            x -= vel
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        if x <= SCREEN_WIDTH - width - vel:
            x += vel
    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -10:
            y -= jump_count
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()