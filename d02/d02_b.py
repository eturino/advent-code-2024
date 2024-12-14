from typing import Literal

from d02.parser import parse_input


def run_d02_b(input_filename: str) -> int:
    valid_count = 0
    for line in parse_input(input_filename):
        if is_valid(line):
            valid_count += 1
        # else:
        #     print(f"Invalid line: {line}")
    # print(f"Valid lines: {valid_count}")
    return valid_count

def is_valid_simple(line: list[int]) -> bool:
    if len(line) < 2:
        return True

    # duplicated values -> nope
    if len(line) > len(set(line)):
        return False

    direction = None
    last_value = None

    for i, x in enumerate(line):
        # first value
        if last_value is None:
            direction = None
            last_value = x
            continue

        valid, new_direction = valid_pair(last_value, x, direction)
        if valid:
            direction = new_direction
            last_value = x
            continue
        return False
    return True

def is_valid(line: list[int]) -> bool:
    if is_valid_simple(line):
        return True
    # trying removing each element one at a time, see if the line is valid
    for i in range(len(line)):
        if is_valid_simple(without_index(line, i)):
            return True
    return False

def without_index[T](line: list[T], index: int) -> list[T]:
    if index < 0 or index >= len(line):
        raise IndexError(f"Index out of range: {index}, line {line}")
    if index == 0:
        return line[1:]
    if index == len(line) - 1:
        return line[:-1]
    return line[:index] + line[index+1:]

# type of literal string values ASC or NEG
Direction = Literal["ASC", "DESC"]


def valid_pair(first: int, second: int, expected_direction: Direction) -> (bool, Direction):
    raw_diff = second - first
    direction = "ASC" if raw_diff > 0 else "DESC"
    abs_diff = abs(raw_diff)
    if abs_diff > 3 or abs_diff < 1:
        return False, direction

    if expected_direction is None:
        return True, direction

    valid = (raw_diff > 0) == (expected_direction == "ASC")
    return valid, direction



if __name__ == "__main__":
    # checking without_index()
    my_list = ['a', 'b', 'c']
    assert (without_index(my_list, 0)) == ['b', 'c']
    assert (without_index(my_list, 1)) == ['a', 'c']
    assert (without_index(my_list, 2)) == ['a', 'b']

    # checking I am not breaking it again
    assert run_d02_b("./sample.txt") == 4
    assert run_d02_b("./sample-extended.txt") == 5

    expected_answer = 311
    assert run_d02_b("./input.txt") == expected_answer
    print(f"Solution: {expected_answer}")
