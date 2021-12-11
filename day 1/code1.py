with open("input.txt") as f:
    raw = f.read()
    array = list(map(lambda x: int(x), raw.split("\n")))
    prev = array[0]
    bigger = 0
    for i in array:
        if i > prev:
            bigger += 1
        prev = i

    print(array)
    print("Bigger: {0}".format(bigger))
