class Weapon():
    def fight(self, opponent: 'Weapon') -> int | None:
        if self.__class__ == opponent.__class__:
            return 3
        return None
    
    def __repr__(self) -> str:
        return self.__class__.__name__


class Rock(Weapon):
    IDENTIFIERS = {'A', 'X'}
    POWER = 1

    def fight(self, opponent: Weapon) -> int:
        result = super().fight(opponent)
        if not result:
            if isinstance(opponent, Scissors):
                result = 6
            else:
                result = 0
        return result + Rock.POWER


class Paper(Weapon):
    IDENTIFIERS = {'B', 'Y'}
    POWER = 2

    def fight(self, opponent: Weapon) -> int:
        result = super().fight(opponent)
        if not result:
            if isinstance(opponent, Rock):
                result = 6
            else:
                result = 0
        return result + Paper.POWER


class Scissors(Weapon):
    IDENTIFIERS = {'C', 'Z'}
    POWER = 3

    def fight(self, opponent: 'Weapon') -> int:
        result = super().fight(opponent)
        if not result:
            if isinstance(opponent, Paper):
                result = 6
            else:
                result = 0
        return result + Scissors.POWER


def weapon_from_identifier(identifier: str) -> Weapon:
    for weapon in [Rock, Paper, Scissors]:
        if identifier in weapon.IDENTIFIERS:
            return weapon()
    raise ValueError(f'Unknown identifier {identifier}')


def load_strategy(filename: str) -> list[tuple[Weapon, Weapon]]:
    strategies = []
    with open(filename, 'r') as file:
        for line in file:
            opponent_id, player_id = line.strip().split()
            player_weapon = weapon_from_identifier(player_id)
            opponent_weapon = weapon_from_identifier(opponent_id)
            strategies.append((player_weapon, opponent_weapon))
    return strategies


def get_score(strategy: list[tuple[Weapon, Weapon]]) -> int:
    score = 0
    for player_weapon, opponent_weapon in strategy:
        score += player_weapon.fight(opponent_weapon)
    return score


strategies = load_strategy('strategy.txt')
print(strategies)
print(get_score(strategies))
