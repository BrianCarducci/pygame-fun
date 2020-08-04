import pygame

class Entity:
    def __init__(self, hitbox, vel, sprite):
        self.vel = vel
        self.sprite = sprite
        self.hitbox = hitbox
