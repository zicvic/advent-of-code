"""AoC 1, 2024."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    column1 = []
    column2 = []
    lines = puzzle_input.splitlines()
    for line in lines:
        values = line.split()
        if len(values) == 2:
            column1.append(int(values[0]))
            column2.append(int(values[1]))
    return [column1, column2]

def sort_data(data):
    """Sort the data."""
    data[0].sort()
    data[1].sort()
    return data[0], data[1]

def part1(data):
    """Solve part 1."""
    left, right = sort_data(data)
    distances = []
    
    for i in range(len(left)):
        distances.append(abs(left[i] - right[i]))
    
    return sum(distances)

def part2(data):
    """Solve part 2."""


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
