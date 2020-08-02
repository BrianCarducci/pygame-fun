import pygame

def setup():
    font = pygame.font.SysFont(None, 24)
    text_surface = font.render("Paused", True, (225, 0, 0), background=None)
    return text_surface