import pygame
from state import State
from entities.entity import Entity


class Player(Entity):
    def __init__(self, hitbox, vel, sprite, entities, stage_location, is_jumping, jump_count):
        self.entities = entities
        self.stage_location = stage_location
        self.is_jumping = is_jumping
        self.jump_count = jump_count
        super().__init__(hitbox, vel, sprite)

    def check_player_actions(self, keys, game_state, screen_width, background_x, background_x2):
        if game_state != State.PAUSED:
            for entity in self.entities:
                if self.hitbox.colliderect(entity.hitbox):
                    print("collision")
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                if self.stage_location > self.hitbox.x:
                    for entity in self.entities:
                        entity.hitbox.x += self.vel
                    self.stage_location -= self.vel
                    background_x += self.vel
                    background_x2 += self.vel
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                for entity in self.entities:
                    entity.hitbox.x -= self.vel
                self.stage_location += self.vel
                background_x -= self.vel
                background_x2 -= self.vel
            if not self.is_jumping:
                if keys[pygame.K_SPACE]:
                    self.is_jumping = True
            else:
                if self.jump_count >= -10:
                    self.hitbox.y -= self.jump_count
                    self.jump_count -= 1
                else:
                    self.is_jumping = False
                    self.jump_count = 10
        return background_x, background_x2

