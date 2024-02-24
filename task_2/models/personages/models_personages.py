from abc import ABC, abstractmethod
from dataclasses import dataclass
import random

@dataclass
class Personage(ABC):
    name: str

    @abstractmethod
    def description_attack(self, text_atack):
        pass

    @abstractmethod
    def speek(self, text_speek):
        pass

    @staticmethod
    def get_random_object(items_objects):
        return items_objects[random.randint(0, len(items_objects)-1)]



@dataclass
class Superhero(Personage):
    weapons: tuple

    def description_attack(self, text_atack, *args):
        weapon_attack = self.get_random_object(self.weapons)
        print(f'{self.name} {text_atack} {weapon_attack.name.lower()}. Слышны звуки:\n- {weapon_attack.print_sound_atack(*args)}!')

    def speek(self, text_speek):
        print(f'{self.name} произносит:\n - {text_speek}! - и с улыбкой подмигивает.')

@dataclass
class Antagonist(Personage):
    tuple_atack_cities: tuple

    def description_attack(self, text_atack):
        print(f'{self.name} {text_atack}')

    def speek(self, text_speek):
        print(f'- {text_speek}!')