"""
--- Day 4: Giant Squid ---
You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. What you can see, however, is a giant squid that has attached itself to the outside of your submarine.

Maybe it wants to play bingo?

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:

7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
Finally, 24 is drawn:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).

The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.

To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?

--- Part Two ---
On the other hand, it might be wise to try a different strategy: let the giant squid win.

You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins, what would its final score be?
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import List, Optional, Set, Tuple

from tqdm import tqdm

INPUT_PATH = Path(__file__).parent / "data/day_04.txt"

TEST_INPUT = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7""".split(
    "\n"
)


class BingoBoard:
    side = 5

    def __init__(self, rows: List[List[int]], cols: List[List[int]]) -> None:
        self.rows = rows
        self.cols = cols
        self.rows_filled = [[False for i in range(self.side)] for i in range(self.side)]
        self.cols_filled = [[False for i in range(self.side)] for i in range(self.side)]
        self.winning_num: Optional[int] = None

    def play_num(self, num: int):

        for row_num, row in enumerate(self.rows):
            for col_num, board_num in enumerate(row):
                if board_num == num:
                    self.rows_filled[row_num][col_num] = True
                    self.cols_filled[col_num][row_num] = True

        is_bingo = self.is_bingo()
        if is_bingo:
            self.winning_num = num

        return is_bingo

    def is_bingo(self) -> bool:
        """Checks row and col of move to see if it makes a bingo"""
        return any([all(row) for row in self.rows_filled]) or any(
            [all(col) for col in self.cols_filled]
        )

    def get_score(self):
        if self.winning_num is None:
            return None

        unmarked_numbers_sum = 0
        for row_num, row in enumerate(self.rows_filled):
            for col_num, val in enumerate(row):
                if not val:
                    unmarked_numbers_sum += self.rows[row_num][col_num]
        score = unmarked_numbers_sum * self.winning_num
        return score

    @classmethod
    def from_strings(cls, strings: List[str]) -> BingoBoard:
        rows = [list(map(int, re.findall("\d+", string))) for string in strings]
        cols = [[row[i] for row in rows] for i in range(cls.side)]
        return cls(rows, cols)

    def __repr__(self) -> str:
        wraps = {True: " ", False: "_"}
        row_strs = []
        for row_num, row in enumerate(self.rows):
            row_str = ""
            for col_num, val in enumerate(row):
                wrap = wraps[self.rows_filled[row_num][col_num]]
                row_str += wrap + f"{val:02d}" + wrap + " "
            row_strs.append(row_str.rstrip(" "))
        return "\n".join(row_strs)

    def get_board_no_state(self) -> str:
        row_strs = []
        for row in self.rows:
            row_str = ""
            for val in row:
                row_str += f"{val:02d} "
            row_strs.append(row_str.rstrip(" "))
        return "\n".join(row_strs)

    def __hash__(self) -> int:
        return hash(self.get_board_no_state())

    def __eq__(self, __o: object) -> bool:
        hash(self) == hash(__o)


def parse_input(path: Path = INPUT_PATH) -> Tuple[List[int], List[BingoBoard]]:
    with open(path) as f:
        data = f.readlines()

    nums, boards = _parse_strings(data)
    return nums, boards


def _parse_strings(data: List[str]) -> Tuple[List[int], Set[BingoBoard]]:
    nums = list(map(int, data[0].replace("\n", "").split(",")))

    boards = set()
    for row_num in range(2, len(data), 6):
        rows = data[row_num : row_num + 5]
        boards.add(BingoBoard.from_strings(rows))
    return nums, boards


def solve_puzzle_1(nums: List[int], boards: List[BingoBoard]) -> int:
    score = None
    for num in nums:
        for board in boards:
            board.play_num(num)
            if board.is_bingo():
                score = board.get_score()
                break
        if score is not None:
            break
    return score


def solve_puzzle_2(nums: List[int], boards: Set[BingoBoard]) -> int:
    ordered_boards = []
    for num in nums:
        if len(boards) == 0:
            break
        to_remove = []
        for board in boards:
            board.play_num(num)
            if board.is_bingo():
                ordered_boards.append(board)
                to_remove.append(board)
        for board in to_remove:
            boards.remove(board)
    return ordered_boards[-1].get_score()


def test_puzzle_1():
    expected_score = 4512
    nums, boards = _parse_strings(TEST_INPUT)
    score = solve_puzzle_1(nums, boards)
    assert (
        score == expected_score
    ), f"puzzle 1 failed with score {score}, expected {expected_score}"


def test_puzzle_2():
    expected_score = 1924
    nums, boards = _parse_strings(TEST_INPUT)
    score = solve_puzzle_2(nums, boards)
    print(f"Test 2 score: {score}")
    assert (
        score == expected_score
    ), f"puzzle 2 failed with score {score}, expected {expected_score}"


test_puzzle_1()
test_puzzle_2()


if __name__ == "__main__":
    nums, boards = parse_input(INPUT_PATH)
    score = solve_puzzle_1(nums, boards)
    print(f"Answer for puzzle 1: {score}")

    second_score = solve_puzzle_2(nums, boards)
    print(f"Answer for puzzle 2: {second_score}")
