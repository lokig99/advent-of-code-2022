def get_priority(letter):
    def lower_letter_priority(letter):
        return ord(letter) - 96

    def upper_letter_priority(letter):
        return ord(letter) - 64 + lower_letter_priority('z')

    if letter.islower():
        return lower_letter_priority(letter)
    return upper_letter_priority(letter)


class Rucksack:
    def __init__(self, content: str):
        self.content = content

    @property
    def first_compartment(self) -> str:
        return self.content[:len(self.content) // 2]

    @property
    def second_compartment(self) -> str:
        return self.content[len(self.content) // 2:]

    def common_items(self) -> list[tuple[str, int]]:
        common_set = set(self.first_compartment).intersection(
            self.second_compartment)
        return [(item, get_priority(item)) for item in common_set]

    def common_items_total_priority(self) -> int:
        return sum([item[1] for item in self.common_items()])

    def common_items_between(self, other: 'Rucksack') -> list[tuple[str, int]]:
        common_set = set(self.content).intersection(other.content)
        return [(item, get_priority(item)) for item in common_set]

    def common_items_between_many(self, others: list['Rucksack']) -> list[tuple[str, int]]:
        common_set = set(self.content)
        for other in others:
            common_set.intersection_update(other.content)
        return [(item, get_priority(item)) for item in common_set]

    def __repr__(self):
        return f'Rucksack({self.first_compartment} | {self.second_compartment})'


def load_rucksack_groups(file_path: str, group_size: int) -> list[list[Rucksack]]:
    rucksack_groups = []
    with open(file_path) as f:
        group = []
        for i, line in enumerate(f):
            rucksack = Rucksack(line.strip())
            if i % group_size == 0 and i != 0:
                rucksack_groups.append(group)
                group = [rucksack]
            else:
                group.append(rucksack)
        if group:
            rucksack_groups.append(group)
    return rucksack_groups


def total_rucksacks_priority(rucksacks: list[Rucksack]) -> int:
    return sum([rucksack.common_items_total_priority() for rucksack in rucksacks])


def common_items_by_group(rucksack_groups: list[list[Rucksack]]) -> list[list[tuple[str, int]]]:
    common_items_by_group = []
    for group in rucksack_groups:
        common_items = group[0].common_items_between_many(group[1:])
        common_items_by_group.append(common_items)
    return common_items_by_group


def common_items_total_priority_all_groups(rucksack_groups: list[list[Rucksack]]) -> int:
    return sum([sum([item[1] for item in group]) for group in common_items_by_group(rucksack_groups)])


rucksack_groups = load_rucksack_groups('rucksacks.txt', 3)

print(common_items_by_group(rucksack_groups))
print(common_items_total_priority_all_groups(rucksack_groups))
