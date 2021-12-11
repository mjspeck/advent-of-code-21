"""
--- Day 5: Hydrothermal Venture ---
You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.

They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:

0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:

An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

So, the horizontal and vertical lines from the above list would produce the following diagram:

.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....
In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

--- Part Two ---
Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.

Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
Considering all lines from the above example would now produce the following diagram:

1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....
You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.

Consider all of the lines. At how many points do at least two lines overlap?
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Counter, Iterable, Literal, Tuple


TEST_INPUT = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""".split(
    "\n"
)

PUZZLE_1_TEST_ANSWER = 5

INPUT_PATH = Path(__file__).parent / "data/day_05.txt"

LineType = Literal["horizontal", "vertical", "diagonal"]


@dataclass
class Point:
    x: int
    y: int

    def __repr__(self) -> str:
        return f"Point: x={self.x}, y={self.y}"

    def __hash__(self) -> int:
        return hash(self.__repr__())


@dataclass
class Line:
    start: Point
    end: Point
    line_type: LineType = field(init=False)
    crossing_points: Tuple[Point] = field(init=False)

    def __post_init__(self):
        self.line_type = self._identify_line_type()
        self.crossing_points = self._get_crossing_points()

    def _identify_line_type(self) -> LineType:
        if self.start.x == self.end.x:
            return "vertical"
        elif self.start.y == self.end.y:
            return "horizontal"
        else:
            return "diagonal"

    def _get_crossing_points(self) -> Tuple[Point]:
        if self.end.x >= self.start.x:
            starting_x = self.start.x
            ending_x = self.end.x
            reverse_x = False
        elif self.end.x < self.start.x:
            starting_x = self.end.x
            ending_x = self.start.x
            reverse_x = True
        if self.end.y >= self.start.y:
            starting_y = self.start.y
            ending_y = self.end.y
            reverse_y = False
        elif self.end.y < self.start.y:
            starting_y = self.end.y
            ending_y = self.start.y
            reverse_y = True
        base_x_iterator = range(starting_x + 1, ending_x)
        base_y_iterator = range(starting_y + 1, ending_y)
        if reverse_x:
            x_iterator = reversed(base_x_iterator)
        else:
            x_iterator = base_x_iterator
        if reverse_y:
            y_iterator = reversed(base_y_iterator)
        else:
            y_iterator = base_y_iterator
        if self.line_type == "horizontal":
            points = tuple([Point(x, self.start.y) for x in x_iterator])
            return points
        elif self.line_type == "vertical":
            points = tuple([Point(self.start.x, y) for y in y_iterator])
            if reverse_y:
                points = tuple(reversed(points))
            return points
        elif self.line_type == "diagonal":
            return tuple(
                [
                    Point(x, y)
                    for x, y in zip(
                        x_iterator,
                        y_iterator,
                    )
                ]
            )

    def get_all_points(self):
        return tuple([self.start]) + self.crossing_points + tuple([self.end])


def parse_line(line: str):
    start, end = line.split("->")
    start_ints = tuple(map(int, start.split(",")))
    end_ints = tuple(map(int, end.split(",")))
    start_point = Point(x=start_ints[0], y=start_ints[1])
    end_point = Point(x=end_ints[0], y=end_ints[1])
    return Line(start_point, end_point)


def parse_lines(lines: Iterable[str]) -> Tuple[Line]:
    return tuple([parse_line(line) for line in lines])


def parse_input() -> Tuple[Line]:
    with open(INPUT_PATH) as f:
        data = f.readlines()
    return parse_lines(data)


def solve_puzzles(lines: Tuple[Line], include_diagonals: bool = False):
    points = tuple()
    if not include_diagonals:
        lines = tuple(filter(lambda x: x.line_type != "diagonal", lines))
    for line in lines:
        points += line.get_all_points()
    counter = Counter(points)
    num_greater_than_2 = len(list(filter(lambda x: x[1] >= 2, counter.items())))
    return num_greater_than_2


def solve_puzzle_1(lines: Tuple[Line]):
    return solve_puzzles(lines)


def solve_puzzle_2(lines: Tuple[Line]):
    return solve_puzzles(lines, True)


def test_puzzle_1():
    test_lines = parse_lines(TEST_INPUT)
    answer = solve_puzzle_1(test_lines)
    assert answer == 5


def test_puzzle_2():
    test_lines = parse_lines(TEST_INPUT)
    answer = solve_puzzle_2(test_lines)
    assert answer == 12


test_puzzle_1()
test_puzzle_2()

if __name__ == "__main__":
    data = parse_input()

    puzzle_1_answer = solve_puzzle_1(data)
    print(f"Puzzle 1 answer: {puzzle_1_answer}")

    puzzle_2_answer = solve_puzzle_2(data)
    print(f"Puzzle 2 answer: {puzzle_2_answer}")
