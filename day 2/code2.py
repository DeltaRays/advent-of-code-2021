import re

with open("input.txt") as f:
    raw = f.read()
    array = raw.split("\n")

    aim = 0
    depth = 0
    x = 0

    for i in array:
        found = re.findall("(\\d+)", i)
        print(found)
        value = int(found[0])
        if i.startswith("forward"):
            depth += aim * value
            x += value
        if i.startswith("down"):
            aim += value
        if i.startswith("up"):
            aim -= value
    print(x * depth)
