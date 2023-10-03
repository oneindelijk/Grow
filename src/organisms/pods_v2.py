from organisms.organic_game_element_v2 import OrganicGameElement

class Pod(OrganicGameElement):
    def __init__(self, x=0, y=0, z30, init_energy_level=0, init_age=0, init_ageing_factor=1.0, spawn_rate=0):
        super().__init__(x=x, y=y, z=z, energy_level=init_energy_level, init_age=init_age, init_ageing_factor=init_ageing_factor)
        self.spawn_rate = spawn_rate

    def spawn(self):
        # Spawning logic for the pod
        pass