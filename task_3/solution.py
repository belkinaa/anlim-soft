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
    name: str
    count_teams: int
    count_teams_in_group: int
    count_person_in_command: int
    list_teams: list = field(init=False, default_factory=list)
    list_groups_teams: list = field(init=False, default_factory=list)

    def registration_commands(self):
        for number_commands in range(1, self.count_teams + 1):
            self.list_teams.append(Team(f'Team#{number_commands}', self.count_person_in_command))

    def round(self):
        self.created_groups()
        self.game_groups()

        list_groups_teams = []
        for group in self.list_groups_teams:
            for team in group.list_teams:
                if team.position < 4:
                    list_groups_teams.append(team)

        list_groups_teams = sorted(list_groups_teams, key=lambda value: value.position)
        for i in range(0, len(list_groups_teams), 2):
            print(f'+--')
            print(list_groups_teams[i])
            if i+1 == len(list_groups_teams):
                break
            print(list_groups_teams[i+1])



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
            print('team:', team)

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
        for group in self.list_groups_teams:
            print('----')
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
        while len(self.list_teams) > 0:
            number_group += 1
            group = Group(f'#{number_group}')
            for _ in range(self.count_teams_in_group):
                group.list_teams.append((random_team := random.choice(self.list_teams)))
                self.list_teams.remove(random_team)
                if len(self.list_teams) == 0:
                    break
            self.list_groups_teams.append(group)

    def __post_init__(self):
        self.registration_commands()

    def round2(self, list_groups_teams):
        map_round = {}
        for team in list_groups_teams:
            if team.position not in map_round:
                map_round[team.position] = [team]
            else:
                map_round[team.position].append(team)

        for k, v in map_round.items():
            print(k, v)




sport_game = Sport_game('Sample_game_name', 11, 4, 1)
sport_game.round()
