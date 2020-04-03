from entities.entity import Entity
import pygame


class Player(Entity):
    def __init__(self, x, y, width, height, vel, is_jumping, jump_count):
        self.is_jumping = is_jumping
        self.jump_count = jump_count
        super().__init__(x, y, width, height, vel)

    def check_player_actions(self, keys, game_state, screen_width):
        if game_state != "paused":
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                if self.x > self.vel:
                    self.x -= self.vel
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                if self.x <= screen_width - self.width - self.vel:
                    self.x += self.vel
            if not self.is_jumping:
                if keys[pygame.K_SPACE]:
                    self.is_jumping = True
            else:
                if self.jump_count >= -10:
                    self.y -= self.jump_count
                    self.jump_count -= 1
                else:
                    self.is_jumping = False
                    self.jump_count = 10

