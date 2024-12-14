from d02.parser import parse_input


def run_d02_a(input_filename: str) -> None:
    valid_count = 0
    for line in parse_input(input_filename):
        if is_valid(line):
            valid_count += 1
    print(f"Valid lines: {valid_count}")


def is_valid(line: list[int]) -> bool:
    direction = None
    last_value = None
    for x in line:
        # first value
        if last_value is None:
            direction = None
            last_value = x
            continue

        elif last_value < x:
            new_direction = "ASC"
        else:
            new_direction = "DESC"

        # check direction
        if direction is not None and direction != new_direction:
            return False

        # check diff
        diff = abs(last_value - x)
        if diff > 3 or diff < 1:
            return False

        # update for new item
        direction = new_direction
        last_value = x
    return True


if __name__ == "__main__":
    run_d02_a("./input.txt")
