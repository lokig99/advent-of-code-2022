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
        middle = len(content) // 2
        self.first_compartment = content[:middle]
        self.second_compartment = content[middle:]

    def common_items(self) -> list[tuple[str, int]]:
        common_set = set(self.first_compartment).intersection(
            self.second_compartment)
        return [(item, get_priority(item)) for item in common_set]

    def common_items_total_priority(self) -> int:
        return sum([item[1] for item in self.common_items()])

    def __repr__(self):
        return f'Rucksack({self.first_compartment} | {self.second_compartment})'


def load_rucksacks(file_path: str) -> list[Rucksack]:
    rucksacks = []
    with open(file_path, 'r') as f:
        for line in f:
            rucksacks.append(Rucksack(line.strip()))
    return rucksacks


def total_rucksacks_priority(rucksacks: list[Rucksack]) -> int:
    return sum([rucksack.common_items_total_priority() for rucksack in rucksacks])


rucksacks = load_rucksacks('rucksacks.txt')
# print(rucksacks)
print(total_rucksacks_priority(rucksacks))
