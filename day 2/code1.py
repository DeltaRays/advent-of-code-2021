import re
from functools import reduce

startingPos = [0, 0]

with open("input.txt") as f:
    raw = f.read()
    forward = reduce(lambda a, b: a + b, map(lambda x: int(x), re.findall("forward (\d*)", raw)))
    down = reduce(lambda a, b: a + b, map(lambda x: int(x), re.findall("down (\d*)", raw)))
    up = reduce(lambda a, b: a + b, map(lambda x: int(x), re.findall("up (\d*)", raw)))
    forward = reduce(lambda a, b: a + b, map(lambda x: int(x), re.findall("forward (\d*)", raw)))
    print(forward*(down-up))
