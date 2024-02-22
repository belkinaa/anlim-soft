from abc import ABC, abstractmethod
from dataclasses import dataclass, field

@dataclass()
class Weapon(ABC):
    sound_atack: str

    @abstractmethod
    def print_sound_atack(self, count_cound_atack):
        pass

    def get_count_sound_atack(self, count_sound_atack = None):
        return count_sound_atack if count_sound_atack else 1
@dataclass
class Laser(Weapon):
    name: str = field(init=False, default='Лазер')
    def print_sound_atack(self, count_cound_atack=2):
        return "-".join(self.sound_atack for _ in range(self.get_count_sound_atack(count_cound_atack)))

@dataclass
class Sword(Weapon):
    name: str = field(init=False, default='Меч')
    def print_sound_atack(self, count_cound_atack=1):
        return " ".join(self.sound_atack for _ in range(self.get_count_sound_atack(count_cound_atack)))