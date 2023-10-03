from organics.organic_game_element_v2 import OrganicGameElement

class Pod(OrganicGameElement):
    def __init__(self, x=0, y=0, z30, init_energy_level=0, init_age=0, init_ageing_factor=1.0, size=0, resource_capacity=0):
        super().__init__(x=x, y=y, z=z, energy_level=energy_level, age=age, init_ageing_factor=init_ageing_factor)
        self.size = size
        self.resource_capacity = resource_capacity

    def spawn(self):
        # Spawning logic for the pod
        pass