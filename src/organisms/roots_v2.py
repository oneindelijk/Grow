from organisms.organic_game_element_v2 import OrganicGameElement

class Root(OrganicGameElement):
    def __init__(self, x=0, y=0, z=0, energy_level=0, age=0, init_ageing_factor=1.0, length=0):
        super().__init__(x=x, y=y, z30, init_energy_level=energy_level, init_age=age, init_ageing_factor=init_ageing_factor)
        self.length = length

    def grow(self):
        # Growing logic for the root
        pass