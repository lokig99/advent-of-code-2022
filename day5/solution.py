class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def move_items(self, dest: 'Stack', cout: int, keep_order: bool = False):
        items_to_move = []
        for _ in range(cout):
            items_to_move.append(self.pop())

        if keep_order:
            items_to_move.reverse()

        for item in items_to_move:
            dest.push(item)

    def top(self):
        return self.items[-1]

    def reverse(self):
        self.items.reverse()

    def copy(self):
        stack = Stack()
        stack.items = self.items[:]
        return stack

    def __repr__(self):
        return f'Stack({self.items})'


class Move:
    def __init__(self, take_from: int, to: int, count: int) -> None:
        self.take_from = take_from
        self.to = to
        self.count = count

    def __repr__(self) -> str:
        return f'Move(from: {self.take_from}, to: {self.to}, count: {self.count})'


def load_crates_from_file(file_name: str) -> dict[int, Stack]:
    def get_column_count(line: str) -> int:
        return round(len(line) / (COLUMN_WIDTH + len(SEPARATOR)))

    COLUMN_WIDTH = 3
    SEPARATOR = ' '
    stacks = {}
    column_count = 0

    with open(file_name) as f:
        for i, line in ((i, l.replace('\n', '')) for i, l in enumerate(f)):
            if i == 0:
                column_count = get_column_count(line)
                for x in range(column_count):
                    stacks[x+1] = Stack()

            if line[:COLUMN_WIDTH].strip().isdigit():
                break

            # load crates
            for x in range(column_count):
                stack = stacks[x+1]
                column_start = x * (COLUMN_WIDTH + len(SEPARATOR))
                column_end = column_start + COLUMN_WIDTH
                crate = line[column_start:column_end].strip()
                if crate:
                    stack.push(crate[1])

    # reverse stacks
    for stack in stacks.values():
        stack.reverse()
    return stacks


def load_moves_from_file(file_name: str) -> list[Move]:
    moves = []
    with open(file_name) as f:
        for line in (l.strip() for l in f):
            if line.startswith('move'):
                count, from_, to = (int(x)
                                    for x in line.split() if x.isdigit())
                moves.append(Move(from_, to, count))
    return moves


def apply_moves(crates: dict[int, Stack], moves: list[Move], keep_order: bool = False) -> dict[int, Stack]:
    output = {x: crates[x].copy() for x in crates.keys()}
    for move in moves:
        output[move.take_from].move_items(
            output[move.to], move.count, keep_order)
    return output


def get_top_crates(crates: dict[int, Stack]) -> str:
    output = ''
    for x in range(1, len(crates)+1):
        stack = crates[x]
        output = f'{output}{stack.top()}'
    return output


crates = load_crates_from_file('crates.txt')
# print(crates)

moves = load_moves_from_file('crates.txt')
# print(moves)

cratemover9000_moved_crates = apply_moves(crates, moves)
# print(crates)
print(f"CrateMover 9000 - Top crates: {get_top_crates(cratemover9000_moved_crates)}")

cratemover9001_moved_crates = apply_moves(crates, moves, keep_order=True)
print(f"CrateMover 9001 - Top crates: {get_top_crates(cratemover9001_moved_crates)}")
