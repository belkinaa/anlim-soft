from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class SMI(ABC):
    name: str


    @abstractmethod
    def sensation(self, message):
        pass

@dataclass
class Journal(SMI):
    def sensation(self, message):
        print(f'Читайте сегодня в выпуске "{self.name}": {message}')

@dataclass
class TV(SMI):
    def sensation(self, message):
        print(f'Смотрите на "{self.name}": {message}!')