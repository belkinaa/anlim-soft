import random
from dataclasses import dataclass, field

@dataclass()
class Position():
    number: str
    point: int

@dataclass()
class Competitor():
    name: str
    name_comand: str
    point: int = field(init=False, default=0)

@dataclass()
class Group():
    name: str
    list_teams: list = field(init=False, default_factory=list)

@dataclass()
class Team():
    name: str
    count_competitor: int
    list_competitors: list = field(init=False, default_factory=list)
    point: int = field(init=False, default=0)
    position: int = field(init=False, default=0)
    list_win_team: list = field(init=False, default_factory=list)
    list_loose_team: list = field(init=False, default_factory=list)
    rating: int = field(init=False, default=0)

    def __post_init__(self):
        [self.list_competitors.append(Competitor(f'Competitor #{_}', self.name)) for _ in range(1, self.count_competitor + 1)]

@dataclass()
class Sport_game():
    """
    :param name : название соревнований
    :param count_teams : количество команд, подавших заявку
    :param count_teams_in_group : количество команд в группе
    :param count_person_in_command : количество игроков в команде (в задании про это ничего нет, но решил просто сделать дополнительно (O_o))
    """
    name: str
    count_teams: int
    count_teams_in_group: int
    count_person_in_command: int

    __registration_list_teams: list = field(init=False, default_factory=list)
    __list_groups_teams: list = field(init=False, default_factory=list)

    @property
    def registration_list_teams(self):
        return self.__registration_list_teams

    @property
    def list_groups_teams(self):
        return self.__list_groups_teams

    def registration_commands(self):
        for number_commands in range(1, self.count_teams + 1):
            self.registration_list_teams.append(Team(f'Team#{number_commands}', self.count_person_in_command))

    def set_rating(self, rating_win, rating_looser, is_win) -> int:
        if is_win:
            return rating_win + (rating_win + rating_looser) / 2
        return rating_looser + (rating_win - rating_looser) / 2

    def play_rounds(self):
        """
        - формирует группы случайным образом
        - моделирует игру команд в группах (случайным образом выявляет победителя)
        - в play_of выходят из групп только команды, занявшие 1, 2 и 3 места с очками 100, 75 и 50 соответственно
        - по умолчанию в play_of сортировка команд по местам
        :return:
        """
        self.created_groups()
        self.game_groups()

        list_groups_teams = []
        for group in self.list_groups_teams:
            for team in group.list_teams:
                if team.position < 4:
                    list_groups_teams.append(team)

        while len(list_groups_teams) > 1:
            list_groups_teams = self.round_play_of(list_groups_teams)
            print('-'*10)

    def round_play_of(self, list_groups_teams, is_rating=False, is_sorting=True) -> list:
        """Формируется и возвращается список победителей игры моделью play_of
        :param list_groups_teams: список команд для игры
        :param is_sorting: делать ли сортировку списка команд
        :param is_rating:  Сортировка групп для игры в play_of по умолчанию по рейтингу. Если указать False, то будет сортировка по месту на основе игр в группах
        :return:
        """
        print(f'Start play_of. Count TEAM:{len(list_groups_teams)}')
        play_of = []
        if is_sorting or is_rating:
            list_groups_teams = sorted(list_groups_teams, key=lambda value: value.rating if is_rating else value.position)

        for i in range(0, len(list_groups_teams), 2):
            team1 = list_groups_teams[i]
            if i+1 == len(list_groups_teams):
                play_of.append(team1)
                break
            team2 = list_groups_teams[i+1]

            if random.randint(0, 1):
                team1.rating = self.set_rating(team1.rating, team2.rating, True)
                team1.list_win_team.append(team2.name)
                team2.rating = self.set_rating(team1.rating, team2.rating, False)
                team2.list_loose_team.append(team1.name)
                play_of.append(team1)
            else:
                team2.rating = self.set_rating(team2.rating, team1.rating, True)
                team2.list_win_team.append(team1.name)
                team1.rating = self.set_rating(team2.rating, team1.rating, False)
                team1.list_loose_team.append(team2.name)
                play_of.append(team2)
        print(f'Result play_of. Count TEAM:{len(play_of)}')
        # Цикл для вывода на экран, чтобы посмотреть на итоги игры. На саму программу никак не влияет
        for team_in_play_of in play_of:
            print(team_in_play_of)
            if len(play_of) == 1:
                team1_team2 = [team1, team2]
                team1_team2.remove(team_in_play_of)
                print(team1_team2[0])

        return play_of

    def set_position_team_group(self, group, position: list) -> None:
        """Устанавливает места командам в группе
        Устанавливает рейтинг"""
        for team in group.list_teams:
            team.position = position.index(team) + 1

            team.rating = {
                1: 100,
                2: 75,
                3: 50
            }.get(team.position, 0)
            print(team)

    def form_list_position_team(self, team, position: list) -> list:
        """Формируется список мест команд на основе "point" и их игр между собой"""
        if position:
            for ind, position_team in enumerate(position):
                if team.point < position_team.point:
                    continue
                elif team.point > position_team.point:
                    position.insert(ind, team)
                    break
                else:
                    if team.name in position_team.list_win_team:
                        position.insert(ind + 1, team)
                        break
                    else:
                        position.insert(ind, team)
                        break
            else:
                position.append(team)
        else:
            position.append(team)
        return position

    def counting_point(self):
        """* Подсчет количества очков у команд в группах.
        * Распределение мест
        * устанавливается рейтинг"""
        for number_group, group in enumerate(self.list_groups_teams, start=1):
            print(f'Result game group#{number_group}:')
            position = []
            for team in group.list_teams:
                team.point = len(team.list_win_team)
                self.form_list_position_team(team, position)
            self.set_position_team_group(group, position)

    def game_groups(self):
        for group in self.list_groups_teams:
            for team1 in group.list_teams:
                for team2 in group.list_teams:
                    if team2 == team1:
                        break
                    if random.randint(0, 1):
                        team1.list_win_team.append(team2.name)
                        team2.list_loose_team.append(team1.name)
                    else:
                        team2.list_win_team.append(team1.name)
                        team1.list_loose_team.append(team2.name)
                    # print(f'ИТОГ: {team1} VS {team2}')
        self.counting_point()

    def created_groups(self):
        number_group = 0
        while len(self.registration_list_teams) > 0:
            number_group += 1
            group = Group(f'#{number_group}')
            for _ in range(self.count_teams_in_group):
                group.list_teams.append((random_team := random.choice(self.registration_list_teams)))
                self.registration_list_teams.remove(random_team)
                if len(self.registration_list_teams) == 0:
                    break
            self.list_groups_teams.append(group)

    def __post_init__(self):
        self.registration_commands()



print('!! В ЗАДАНИИ НАПСАНО СОРТИРОВКА В play_of ПО МЕСТАМ РЕЗУЛЬТАТА ИГР ГРУПП. ОДНАКО ЕСЛИ БУДЕТ НЕЧЕТНОЕ КОЛИЧЕСТВО КОМАНД, ТО ПОСЛЕДНЯЯ КОМАНДА В play_of БУДЕТ ИГРАТЬ ТОЛЬКО 1 ИГРУ - С ПОБЕДИТЕЛЕМ ВСЕХ ИГР play_of!')
print('!! ТАКЖЕ В ЗАДАНИИ НЕТ ТЬОЧНОЙ ФОРМУЛЫ РАСЧЕТА РЕЙТИНГА, ПОЭТОМУ БЫЛА ПРИДУМАНА СВОЯ (О_o)')
sport_game = Sport_game('Sample_game_name', 11, 4, 1)
sport_game.play_rounds()
