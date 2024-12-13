
from d01.parser import parse_input


def run_d01_b(input_filename: str) -> None:
    list_a, _, count_b = parse_input(input_filename)
    # calculate values
    total_value = 0
    for num_a in list_a:
        total_value += num_a * count_b[num_a]
    print("Total value:", total_value)


if __name__ == "__main__":
    run_d01_b("./input.txt")
