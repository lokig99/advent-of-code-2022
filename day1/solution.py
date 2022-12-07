from dataclasses import dataclass


@dataclass
class Elf:
    id: int
    calories: int


def read_calories() -> list[Elf]:
    elfs: list[Elf] = []
    index = 0
    with open('calories.txt', 'r') as file:
        cals = 0
        for line in file:
            line = line.strip()
            if line.isnumeric():
                cals += int(line)
            else:
                elfs.append(Elf(index, cals))
                index += 1
                cals = 0
        if cals:
            elfs.append(Elf(index, cals))
    return elfs


def get_top_elfs_calories(elfs: list[Elf], top: int) -> int:
    def sort_elfs(elfs: list[Elf]) -> list[Elf]:
        return sorted(elfs, key=lambda elf: elf.calories, reverse=True)
    return sum(elf.calories for elf in sort_elfs(elfs)[:top])


print(get_top_elfs_calories(read_calories(), 3))
