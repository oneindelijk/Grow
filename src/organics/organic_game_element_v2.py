from math import pow
from game_elements.base_game_element import BaseGameElement

class OrganicGameElement(BaseGameElement):
    def __init__(self, x=0, y=0, z=0, energy_level=0, age=0, init_ageing_factor=1.0):
        super().__init__(x=x, y=y, z=z)
        self.energy_level = energy_level
        self.age = age
        self.init_ageing_factor = init_ageing_factor

    def performance_curve(self):
        # Formula involving energy_level, init_ageing_factor and age
        return pow(self.energy_level, self.age / self.init_ageing_factor)

    def update(self):
        # Update the organic element's energy level and age
        self.age += 1
        self.energy_level = self.performance_curve()