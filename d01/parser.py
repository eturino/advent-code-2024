import re
from collections import defaultdict

RE_SPACES = r"\s+"


def parse_input(input_filename: str) -> (list[int], list[int], dict[int, int]):
    with open(input_filename, "r") as f:
        list_a: list[int] = []
        list_b: list[int] = []
        count_b: dict[int, int] = defaultdict(lambda: 0)
        lines = f.readlines()
        for line in lines:
            res = re.split(RE_SPACES, line)
            if len(res) >= 2 and res[0] != "" and res[1] != "":
                num_a = int(res[0])
                num_b = int(res[1])
                list_a.append(num_a)
                list_b.append(num_b)
                count_b[num_b] += 1
        return list_a, list_b, count_b
