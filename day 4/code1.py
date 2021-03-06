import re


def hasWon(bingo_board: list[list[tuple[str, bool]]], bingo_moves: list[str]):
    row_count = len(bingo_board)
    column_count = len(bingo_board[0])

    # Row loop
    for i in range(row_count - 1):
        current_row = bingo_board[i]
        row_elements_remaining = column_count
        # Loop to check the number of row elements that still haven't been matched
        for move in bingo_moves:
            for row_item in current_row:
                if row_item == move:
                    row_elements_remaining -= 1
        if row_elements_remaining == 0:
            return True
    # Column loop
    for i in range(column_count - 1):
        col_elements_remaining = row_count
        for j in range(row_count - 1):
            for move in bingo_moves:
                if bingo_board[j][i] == move:
                    col_elements_remaining -= 1
        if col_elements_remaining == 0:
            return True
    return False


with open("input.txt") as file:
    raw = file.read()
    raw_data = raw.split("\n\n")
    total_bingo_moves = raw_data.pop(0).split(",")
    # Messy one-liner used to convert the input into a list of boards which are a list of rows which are a list of
    # tuples. The first tuple element is the number, the second whether or not it's been drawn yet There are other
    # ways to implement this that are probably more efficient but I'm not going for efficiency
    bingo_boards = list(
        map(lambda x: list(map(lambda y: re.split("\\s+", y), x.split("\n"))),
            raw_data))
    last_winner_rounds = len(total_bingo_moves) + 1
    winner_board = None
    for board in bingo_boards:
        winning_round = len(total_bingo_moves) + 1
        for i in range(len(total_bingo_moves)):
            if hasWon(board, total_bingo_moves[:i + 1]):
                winning_round = i + 1
                break
        if winning_round < last_winner_rounds:
            last_winner_rounds = winning_round
            winner_board = board
    total_score = 0
    for winner_row in winner_board:
        for winner_item in winner_row:
            is_unmarked = True
            for bingo_move in total_bingo_moves[:last_winner_rounds]:
                if winner_item == bingo_move:
                    is_unmarked = False
            if is_unmarked:
                total_score += int(winner_item)
    print(winner_board)
    print("Answer: {}".format(int(total_bingo_moves[last_winner_rounds - 1]) * total_score))
