with open("input.txt") as f:
    raw = f.read()
    array = list(map(lambda x: int(x), raw.split("\n")))
    firstPrev = array[0]
    secondPrev = array[1]
    thirdPrev = array[2]
    bigger = 0
    for i in range(len(array) - 2):
        old = firstPrev + secondPrev + thirdPrev
        firstPrev = array[i]
        secondPrev = array[i + 1]
        thirdPrev = array[i + 2]
        new = firstPrev + secondPrev + thirdPrev
        if new > old:
            bigger += 1
    print(bigger)
