import re

with open("input.txt") as file:
    raw = file.read()
    rawData = raw.split("\n\n")
    bingoMoves = rawData.pop(0).split(",")
    bingoBoards = list(map(lambda x: list(map(lambda y: re.split("\\s+", y), x.split("\n"))), rawData))
    print(bingoMoves)
    print(bingoBoards)
