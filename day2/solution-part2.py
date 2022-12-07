class Weapon():
    def fight(self, opponent: 'Weapon') -> int | None:
        if self.__class__ == opponent.__class__:
            return 3
        return None

    def __repr__(self) -> str:
        return self.__class__.__name__


class Rock(Weapon):
    IDENTIFIER = 'A'
    POWER = 1
    LOSES_TO = 'B'
    WINS_WITH = 'C'

    def fight(self, opponent: Weapon) -> int:
        result = super().fight(opponent)
        if not result:
            if isinstance(opponent, Scissors):
                result = 6
            else:
                result = 0
        return result + Rock.POWER


class Paper(Weapon):
    IDENTIFIER = 'B'
    POWER = 2
    LOSES_TO = 'C'
    WINS_WITH = 'A'

    def fight(self, opponent: Weapon) -> int:
        result = super().fight(opponent)
        if not result:
            if isinstance(opponent, Rock):
                result = 6
            else:
                result = 0
        return result + Paper.POWER


class Scissors(Weapon):
    IDENTIFIER = 'C'
    POWER = 3
    LOSES_TO = 'A'
    WINS_WITH = 'B'

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
        if identifier == weapon.IDENTIFIER:
            return weapon()
    raise ValueError(f'Unknown identifier {identifier}')


def weapon_from_battle_result(result: str, opponent: Weapon) -> Weapon:
    """ result: `X` - loose, `Y` - draw, `Z` - win """
    if result == 'X':
        return weapon_from_identifier(opponent.WINS_WITH)
    elif result == 'Y':
        return weapon_from_identifier(opponent.IDENTIFIER)
    elif result == 'Z':
        return weapon_from_identifier(opponent.LOSES_TO)
    raise ValueError(f'Unknown result {result}')


def load_strategy(filename: str) -> list[tuple[Weapon, Weapon]]:
    strategies = []
    with open(filename, 'r') as file:
        for line in file:
            opponent_id, battle_result = line.strip().split()
            opponent_weapon = weapon_from_identifier(opponent_id)
            player_weapon = weapon_from_battle_result(battle_result, opponent_weapon)
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
