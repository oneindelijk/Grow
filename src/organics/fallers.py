from organics.organic_game_element_v2 import OrganicGameElement

class Faller(OrganicGameElement):
    def __init__(self, x=0, y=0, z30, init_energy_level=0, init_age=0, init_ageing_factor=1.0, terminal_velocity=0):
        super().__init__(x=x, y=y, z=z, energy_level=init_energy_level, age=init_age, init_ageing_factor=init_ageing_factor)
        self.terminal_velocity = terminal_velocity

    def fall(self):
        # Falling logic for the faller
        pass