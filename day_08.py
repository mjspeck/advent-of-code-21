"""
--- Day 8: Seven Segment Search ---
You barely reach the safety of the cave when the whale smashes into the cave mouth, collapsing it. Sensors indicate another exit to this cave at a much greater depth, so you have no choice but to press on.

As your submarine slowly makes its way through the cave system, you notice that the four-digit seven-segment displays in your submarine are malfunctioning; they must have been damaged during the escape. You'll be in a lot of trouble without them, so you'd better figure out what's wrong.

Each digit of a seven-segment display is rendered by turning on or off any of seven segments named a through g:

  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
So, to render a 1, only segments c and f would be turned on; the rest would be off. To render a 7, only segments a, c, and f would be turned on.

The problem is that the signals which control the segments have been mixed up on each display. The submarine is still trying to display numbers by producing output on signal wires a through g, but those wires are connected to segments randomly. Worse, the wire/segment connections are mixed up separately for each four-digit display! (All of the digits within a display use the same connections, though.)

So, you might know that only signal wires b and g are turned on, but that doesn't mean segments b and g are turned on: the only digit that uses two segments is 1, so it must mean segments c and f are meant to be on. With just that information, you still can't tell which wire (b/g) goes to which segment (c/f). For that, you'll need to collect more information.

For each display, you watch the changing signals for a while, make a note of all ten unique signal patterns you see, and then write down a single four digit output value (your puzzle input). Using the signal patterns, you should be able to work out which pattern corresponds to which digit.

For example, here is what you might see in a single entry in your notes:

acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
cdfeb fcadb cdfeb cdbaf
(The entry is wrapped here to two lines so it fits; in your notes, it will all be on a single line.)

Each entry consists of ten unique signal patterns, a | delimiter, and finally the four digit output value. Within an entry, the same wire/segment connections are used (but you don't know what the connections actually are). The unique signal patterns correspond to the ten different ways the submarine tries to render a digit using the current wire/segment connections. Because 7 is the only digit that uses three segments, dab in the above example means that to render a 7, signal lines d, a, and b are on. Because 4 is the only digit that uses four segments, eafb means that to render a 4, signal lines e, a, f, and b are on.

Using this information, you should be able to work out which combination of signal wires corresponds to each of the ten digits. Then, you can decode the four digit output value. Unfortunately, in the above example, all of the digits in the output value (cdfeb fcadb cdfeb cdbaf) use five segments and are more difficult to deduce.

For now, focus on the easy digits. Consider this larger example:

be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |
fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |
fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |
cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |
efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |
gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |
gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |
cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |
ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |
gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |
fgae cfgab fg bagce
Because the digits 1, 4, 7, and 8 each use a unique number of segments, you should be able to tell which combinations of signals correspond to those digits. Counting only digits in the output values (the part after | on each line), in the above example, there are 26 instances of digits that use a unique number of segments (highlighted above).

In the output values, how many times do digits 1, 4, 7, or 8 appear?

--- Part Two ---
Through a little deduction, you should now be able to determine the remaining digits. Consider again the first example above:

acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
cdfeb fcadb cdfeb cdbaf
After some careful analysis, the mapping between signal wires and segments only make sense in the following configuration:

 dddd
e    a
e    a
 ffff
g    b
g    b
 cccc
So, the unique signal patterns would correspond to the following digits:

acedgfb: 8
cdfbe: 5
gcdfa: 2
fbcad: 3
dab: 7
cefabd: 9
cdfgeb: 6
eafb: 4
cagedb: 0
ab: 1
Then, the four digits of the output value can be decoded:

cdfeb: 5
fcadb: 3
cdfeb: 5
cdbaf: 3
Therefore, the output value for this entry is 5353.

Following this same process for each entry in the second, larger example above, the output value of each entry can be determined:

fdgacbe cefdb cefbgd gcbe: 8394
fcgedb cgb dgebacf gc: 9781
cg cg fdcagb cbg: 1197
efabcd cedba gadfec cb: 9361
gecf egdcabf bgf bfgea: 4873
gebdcfa ecba ca fadegcb: 8418
cefg dcbef fcge gbcadfe: 4548
ed bcgafe cdgba cbgef: 1625
gbdfcae bgc cg cgb: 8717
fgae cfgab fg bagce: 4315
Adding all of the output values in this larger example produces 61229.

For each entry, determine all of the wire/segment connections and decode the four-digit output values. What do you get if you add up all of the output values?
"""

from collections import defaultdict
from copy import copy
from typing import Dict, List, Set, Tuple

from utils import get_input_path

INPUT_PATH = get_input_path(__file__)

DIGITS = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9",
}

LETTERS = "abcdefg"

TEST_INPUT = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce""".split(
    "\n"
)


def parse_input(input_strings: List[str]) -> Tuple[List[List[str]], List[List[str]]]:
    inputs, outputs = list(zip(*map(lambda x: x.split(" | "), input_strings)))
    inputs = list(map(lambda x: x.split(), inputs))
    outputs = list(map(lambda x: x.split(), outputs))
    return inputs, outputs


def solve_puzzle_1(outputs: List[List[str]]) -> int:
    counts = 0
    for output_sequence in outputs:
        for output in output_sequence:
            if len(output) in [2, 3, 4, 7]:
                counts += 1
    return counts


def solve_puzzle_2(inputs: List[List[str]], outputs: List[List[str]]) -> int:
    outputs_sum = 0
    for input_sequence, output_sequence in zip(inputs, outputs):
        mapping = get_entry_letter_mappings(input_sequence)
        full_output = ""
        for output in output_sequence:
            digit = map_output_to_digit(output, mapping)
            full_output += digit
        output_num = int(full_output)
        outputs_sum += output_num
    return outputs_sum


def get_entry_letter_mappings(single_input: List[str]) -> Dict[str, str]:

    """
    steps:
    identify a: in 3-digit number but not in 2-digit number
    identify d: in all 5-digit numbers, but only in 2 6-digit numbers
    identify c: only letter in two 5-digit and two 6-digit numbers
    identify f: other letter in 2-digit number
    identify g: only other number in all 6-digit and 5-digit numbers that isn't a
    identify b: in all 6-digit and only 1 5-digit
    identify e: only one remaining
    """
    remaining_letters = copy(LETTERS)
    true_mappings = {}

    lens: defaultdict[int, List[Set]] = defaultdict(list)

    for i in single_input:
        lens[len(i)].append(set(i))

    assert len(lens[2]) == 1, "failed for lens 2"
    assert len(lens[3]) == 1, "failed for lens 3"
    assert len(lens[4]) == 1, "failed for lens 4"
    assert len(lens[5]) == 3, "failed for lens 5"
    assert len(lens[6]) == 3, "failed for lens 6"
    assert len(lens[7]) == 1, "failed for lens 7"

    # identify a: in 3-digit number but not in 2-digit number

    three_minus_2 = lens[3][0] - lens[2][0]
    assert len(three_minus_2) == 1, "identifying a failed"
    true_mappings["a"] = three_minus_2.pop()
    remaining_letters = remaining_letters.replace(true_mappings["a"], "")

    # identify d: in all 5-digit numbers, but only in two 6-digit numbers
    for letter in remaining_letters:
        in_all_5 = all([letter in thing for thing in lens[5]])
        in_two_2 = len(list(filter(lambda x: letter in x, lens[6]))) == 2
        if in_all_5 and in_two_2:
            true_mappings["d"] = letter
            break
    remaining_letters = remaining_letters.replace(true_mappings["d"], "")

    # identify c: only letter in two 5-digit and two 6-digit numbers
    for letter in remaining_letters:
        in_two_5 = len(list(filter(lambda x: letter in x, lens[5]))) == 2
        in_two_6 = len(list(filter(lambda x: letter in x, lens[6]))) == 2

        if in_two_5 and in_two_6:
            true_mappings["c"] = letter
            break
    remaining_letters = remaining_letters.replace(true_mappings["c"], "")

    # identify f: other letter in 2-digit number

    two_letter = copy(lens[2]).pop()
    for letter in remaining_letters:
        if letter in two_letter:
            true_mappings["f"] = letter
            break
    remaining_letters = remaining_letters.replace(true_mappings["f"], "")

    # identify g: only other number in all 6-digit and 5-digit numbers that isn't a

    for letter in remaining_letters:
        in_all_6 = all([letter in x for x in lens[6]])
        in_all_5 = all([letter in x for x in lens[5]])

        if in_all_6 and in_all_5:
            true_mappings["g"] = letter
            break
    remaining_letters = remaining_letters.replace(true_mappings["g"], "")

    # identify b: in all 6-digit and only one 5-digit

    for letter in remaining_letters:
        in_all_6 = all([letter in x for x in lens[6]])
        in_one_5 = len(list(filter(lambda x: letter in x, lens[5]))) == 1

        if in_all_6 and in_one_5:
            true_mappings["b"] = letter
            break
    remaining_letters = remaining_letters.replace(true_mappings["b"], "")

    # identify e: last remaining
    true_mappings["e"] = remaining_letters
    reversed_mappings = {value: key for (key, value) in true_mappings.items()}
    return reversed_mappings


def map_output_to_digit(output: str, mapping: Dict[str, str]) -> str:
    correct_output = ""
    for letter in output:
        correct_output += mapping[letter]

    correct_output_sorted = "".join(sorted(correct_output))
    digit = DIGITS[correct_output_sorted]
    return digit


def test_puzzle_1():
    expected_score = 26
    _, outputs = parse_input(TEST_INPUT)
    answer = solve_puzzle_1(outputs)
    assert (
        answer == expected_score
    ), f"Puzzle 1 failed with answer {answer}, expected {expected_score}"


def test_puzzle_2():
    expected_score = 61229
    inputs, outputs = parse_input(TEST_INPUT)
    answer = solve_puzzle_2(inputs, outputs)
    assert (
        answer == expected_score
    ), f"Puzzle 2 failed with answer {answer}, expected {expected_score}"


test_puzzle_1()
test_puzzle_2()


if __name__ == "__main__":

    with open(INPUT_PATH) as f:
        data = f.readlines()
    inputs, outputs = parse_input(data)

    puzzle_1_answer = solve_puzzle_1(outputs)
    print(f"Answer for puzzle 1: {puzzle_1_answer}")

    puzzle_2_answer = solve_puzzle_2(inputs, outputs)
    print(f"Answer for puzzle 1: {puzzle_2_answer}")
