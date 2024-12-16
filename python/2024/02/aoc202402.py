"""AoC 2, 2024."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    lines = puzzle_input.splitlines()
    data = []
    for line in lines:
        values = list(map(int, line.split()))
        data.append(values)
    return data


def part1(data):
    """Solve part 1."""
    safe_count = 0
    
    for report in [[line[i+1] - line[i] for i in range(len(line)-1)] for line in data]:
        if all(1 <= abs(x) <= 3 for x in report) and (all(x > 0 for x in report) or all(x < 0 for x in report)):
            safe_count += 1
    return safe_count


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
