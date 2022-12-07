class SectionRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __len__(self):
        return self.end - self.start + 1

    def __repr__(self):
        return f"SectionRange({self.start}, {self.end})"
    
    def fully_contains(self, other: 'SectionRange'):
        if len(self) >= len(other):
            return self.start <= other.start and self.end >= other.end
        
    def overlaps(self, other: 'SectionRange'):
        return self.start <= other.end and self.end >= other.start
        

def load_sectionrange_pairs(filename: str) -> list[tuple[SectionRange, SectionRange]]:
    section_pairs = []
    with open(filename) as f:
        for line in (l.strip() for l in f):
            first, second = line.split(',')
            first_start, first_end = first.split('-')
            second_start, second_end = second.split('-')
            first_range = SectionRange(int(first_start), int(first_end))
            second_range = SectionRange(int(second_start), int(second_end))
            section_pairs.append((first_range, second_range))
    return section_pairs


def fully_contained_pairs_count(section_pairs: list[tuple[SectionRange, SectionRange]]) -> int:
    count = 0
    for first, second in section_pairs:
        if first.fully_contains(second) or second.fully_contains(first):
            count += 1
    return count

def overlapping_pairs_count(section_pairs: list[tuple[SectionRange, SectionRange]]) -> int:
    count = 0
    for first, second in section_pairs:
        if first.overlaps(second):
            count += 1
    return count



sections = load_sectionrange_pairs('sections.txt')
print(sections)
print(fully_contained_pairs_count(sections))
print(overlapping_pairs_count(sections))

