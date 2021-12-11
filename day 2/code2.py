import re

with open("input.txt") as f:
    raw = f.read()
    array = raw.split("\n")

    aim = 0
    depth = 0
    x = 0

    for i in array:
        found = re.findall("(\\d+)", i)
        value = int(found[0])
        if i.startswith("forward"):
            depth += aim * value
            x += value
        elif i.startswith("down"):
            aim += value
        elif i.startswith("up"):
            aim -= value
    print("Result: {}".format(x * depth))
