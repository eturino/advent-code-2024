from d01.parser import parse_input


def run_d01_a(input_filename: str) -> None:
    list_a, list_b, _ = parse_input(input_filename)
    list_a = sorted(list_a)
    list_b = sorted(list_b)
    # ensure same length
    if len(list_a) != len(list_b):
        print("Lists are not of equal length")
        return
    # calculate distances
    total_distance = 0
    for i in range(len(list_a)):
        total_distance += abs(list_a[i] - list_b[i])
    print(f"Total distance: {total_distance}")


if __name__ == "__main__":
    run_d01_a("./input.txt")
