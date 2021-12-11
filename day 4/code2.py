# From here on I'll use better python methods since I've gotten used to the basic syntax
import re


def parse_input(raw: str) -> (list[int], list[str]):
    arr = raw.split("\n\n")
    total_bingo_moves = list(map(lambda move: int(move), arr.pop(0).split(",")))
    bingo_boards = arr
    return total_bingo_moves, bingo_boards


class Board:

    def __init__(self, data: list[list[int]]):
        self.data = data
        self.row_count = len(data)
        self.col_count = len(data[0])
        self.marked = [[False] * self.col_count for i in range(self.row_count)]

    def mark_num(self, number: int):
        for row in range(self.row_count):
            for col in range(self.col_count):
                if self.data[row][col] == number:
                    self.marked[row][col] = True

    def has_won(self) -> bool:
        # Checks rows (the meaning of this code is 'any_row_won is whether all columns in any row are marked')
        any_row_won = any(all(self.marked[row][col] for col in range(self.col_count)) for row in range(self.row_count))
        # Checks columns (the meaning of this code is 'any_row_won is whether all rows in any column are marked')
        any_col_won = any(all(self.marked[row][col] for row in range(self.row_count)) for col in range(self.col_count))
        return any_row_won or any_col_won

    def sum_unmarked(self) -> int:
        # Long method
        """
        total = 0
        for row in range(self.row_count):
            for col in range(self.col_count):
                if not self.marked[row][col]:
                    total += self.data[row][col]
        return total
        """
        # Short method
        return sum(sum(self.data[row][col] for col in range(self.col_count) if not self.marked[row][col]) for row in
                   range(self.row_count))

    @classmethod
    def deserialize(cls, data: str):
        parsed = list(map(
            lambda row: list(map(lambda value: int(value), re.split("\\s+", str.strip(row))))
            , data.split("\n")))
        return cls(parsed)


if __name__ == "__main__":
    with open("input.txt") as file:
        raw_data = file.read()
    with open("example.txt") as file:
        raw_example_data = file.read()

    # A variable used to choose which one of the two to use
    # Example data is used to see if the code works
    use_example_data = False

    bingo_moves, raw_boards = parse_input(raw_example_data if use_example_data else raw_data)

    boards = [Board.deserialize(board) for board in raw_boards]
    boards_won = [False] * len(boards)

    # We need to find the last board which wins
    for number in bingo_moves:
        for i, board in enumerate(boards):
            board.mark_num(number)
            if board.has_won():
                boards_won[i] = True
                if all(boards_won):
                    print(f"{number} was the number picked that made the last board win!")
                    print("Score: {}".format(board.sum_unmarked() * number))
                    exit()
