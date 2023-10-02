from organisms.organic_game_element_v2 import OrganicGameElement

class Seed(OrganicGameElement):
    def __init__(self, x=0, y=0, z=0, energy_level=0, age=0, init_ageing_factor=1.0, size=0):
        super().__init__(x=x, y=y, z=z, energy_level=energy_level, age=age, init_ageing_factor=init_ageing_factor)
        self.size = size

    def sprout(self):
        # Sprouting logic for the seed
        pass