# Base class for all game elements with spatial coordinates
class BaseGameElement:
    def __init__(self, x=0, y=0, z=0):
        # Initial spatial coordinates
        self.x = x
        self.y = y
        self.z = z

    def move(self, dx_step, xy_step, zh_step):
        # Move the game element in space
        self.x += dx_step
        self.y += dy_step
        self.z += dh_step
