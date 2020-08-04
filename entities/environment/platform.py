from entities.entity import Entity

class Platform(Entity):
    def __init__(self, hitbox, vel, sprite, stage_location):
        self.stage_location = stage_location
        super().__init__(hitbox, vel, sprite)

