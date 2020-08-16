import pygame
from state import State
from entities.entity import Entity
from entities.environment.platform import Platform




class Player(Entity):
    collision_side = ""
    colliding_entity = None
    collisions = []

    def __init__(self, hitbox, vel, sprite, stage_location, is_jumping, base_jump_count, jump_count, is_falling):
        self.stage_location = stage_location
        self.is_jumping = is_jumping
        self.base_jump_count = base_jump_count
        self.jump_count = jump_count
        self.is_falling = is_falling
        super().__init__(hitbox, vel, sprite)

    def check_player_actions(self, entities, keys, game_state, screen_width, background_x, background_x2):
        if game_state != State.PAUSED:
            self.check_player_collisions(entities)
            
            # Check if falling
            if not self.is_jumping and {"collision_side": "bottom", "colliding_entity": Platform} not in self.collisions:
                self.is_falling = True
                self.hitbox.y += self.jump_count
            else:
                self.is_falling = False

            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                if {"collision_side": "left", "colliding_entity": Platform} not in self.collisions:
                    if self.stage_location > self.hitbox.x:
                        for entity in entities:
                            entity.hitbox.x += self.vel
                        self.stage_location -= self.vel
                        background_x += self.vel
                        background_x2 += self.vel

            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                if {"collision_side": "right", "colliding_entity": Platform} not in self.collisions:
                    for entity in entities:
                        entity.hitbox.x -= self.vel
                    self.stage_location += self.vel
                    background_x -= self.vel
                    background_x2 -= self.vel

            if not self.is_jumping and not self.is_falling:
                if keys[pygame.K_SPACE]:
                    self.is_jumping = True
            else:
                if self.jump_count <= 0:
                    if {"collision_side": "bottom", "colliding_entity": Platform} in self.collisions:
                        self.is_jumping = False
                        self.jump_count = self.base_jump_count
                if self.jump_count >= self.base_jump_count*-1 and self.is_jumping:
                    self.hitbox.y -= self.jump_count
                    self.jump_count -= 1
                else:
                    self.is_jumping = False
                    self.jump_count = self.base_jump_count
                    
        return background_x, background_x2


    def check_player_collisions(self, entities):
        print(self.vel)
        self.collisions = []
        for entity in entities:
            if self.hitbox.colliderect(entity.hitbox):
                if self.hitbox.bottom <= entity.hitbox.top + self.jump_count:
                    self.collision_side = "bottom"
                elif self.hitbox.right > entity.hitbox.right:
                    self.collision_side = "left"
                elif self.hitbox.left - self.vel < entity.hitbox.left:
                    self.collision_side = "right"
                self.collisions.append(
                    {
                        "collision_side": self.collision_side,
                        "colliding_entity": type(entity)
                    }
                )
                
    def is_dead(self, window_height):
        return self.hitbox.top >= window_height
        

                    


