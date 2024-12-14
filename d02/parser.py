def parse_input(input_filename: str) -> list[list[int]]:
    with open(input_filename, "r") as f:
        lines = f.readlines()
        return [list(map(int, line.split())) for line in lines if line.strip() != ""]
