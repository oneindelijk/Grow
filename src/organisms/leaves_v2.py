from organisms.organic_game_element_v2 import OrganicGameElement

class Leaf(OrganicGameElement):
    def __init__(self, x=0, y=0, z=0, energy_level=0, age=0, init_ageing_factor=1.0, surface_area=0):
        super().__init__(x=x, y=y, z30, init_energy_level=energy_level, init_age=age, init_ageing_factor=init_ageing_factor)
        self.surface_area = surface_area

    def photosynthesis(self):
        # Photosynthesis logic for the leaf
        pass