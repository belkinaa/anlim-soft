import random

from task_2.models.personages import Superhero, Antagonist
from task_2.models.weapons import Laser, Sword
from task_2.models.cities import City
from task_2.models.smi import Journal, TV


superhero = Superhero('Чак-Норис', (Laser('ПИУ'),
                                    Sword('ВЖУХ')))

antagonist = Antagonist('Годзилла', (City('Кострома'),
                                     City('Токио'),
                                     City('Тюмень')))

all_smi = (Journal('ЯЖ ЭТО ВИДЕЛ'), TV("Первый канал"))
smi = all_smi[random.randint(0, len(all_smi)-1)]

atacked_city = antagonist.get_random_object(antagonist.tuple_atack_cities)
antagonist.description_attack(f'стоит возле небоскреба {atacked_city.name}:')
antagonist.speek('АРРРР')
superhero.description_attack('достает свой любимый')
smi.sensation(f'{superhero.name} спас {atacked_city.name}')

