def solve(input: str, distinct_count: int) -> int:
    for offset in range(0, len(input) - distinct_count):
        chunk = set(input[offset:offset + distinct_count])
        if len(chunk) == distinct_count:
            return offset + distinct_count
    return -1

def load_input(file_name: str) -> str:
    with open(file_name, 'r') as f:
        return f.read()


if __name__ == '__main__':
    input = load_input('input.txt')
    print(solve(input, 4))
    print(solve(input, 14))
        
            
            
        