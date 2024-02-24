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


    def counting_point(self):
        for group in self.list_groups_teams:
            for team in group.list_teams:
                team.point = len(team.list_win_team)
                print('team:', team)


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
                    print(f'ИТОГ: {team1} VS {team2}')
        print('----')
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



sport_game = Sport_game('Sample_game_name', 10, 4, 1)
sport_game.round()
