"""Tests for AoC 1, 2024."""

# Standard library imports
import pathlib

# Third party imports
import aoc202401
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202401.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc202401.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [[3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3]]
    assert type(example1[0][0]) == int


def test_sort_data(example1):
    """Test that data is sorted properly."""
    assert aoc202401.sort_data(example1) == ([1, 2, 3, 3, 3, 4], [3, 3, 3, 4, 5, 9])

def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202401.part1(example1) == 11


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202401.part2(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc202401.part2(example2) == ...
