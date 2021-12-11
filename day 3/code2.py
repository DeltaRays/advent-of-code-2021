with open("input.txt") as f:
    raw = f.read()
    o2GenRating = raw.split("\n")
    co2ScrubberRating = raw.split("\n")

    for i in range(len(o2GenRating[0])):
        withZero = []
        withOne = []
        for j in range(len(o2GenRating)):
            currentN = o2GenRating[j]
            interestingBit = currentN[i]
            if interestingBit == '1':
                withOne.append(currentN)
            else:
                withZero.append(currentN)
        if len(withZero) > len(withOne):
            o2GenRating = withZero
        else:
            o2GenRating = withOne

    for i in range(len(co2ScrubberRating[0])):
        withZero = []
        withOne = []
        for j in range(len(co2ScrubberRating)):
            currentN = co2ScrubberRating[j]
            interestingBit = currentN[i]
            if interestingBit == '1':
                withOne.append(currentN)
            else:
                withZero.append(currentN)
        print(len(withZero), len(withOne))
        if len(withZero) == 0 and len(withOne) == 1:
            co2ScrubberRating = withOne
            break
        if len(withZero) == 1 and len(withOne) == 0:
            co2ScrubberRating = withZero
            break
        if len(withZero) <= len(withOne):
            co2ScrubberRating = withZero
        else:
            co2ScrubberRating = withOne

    o2DecimalRating = int(o2GenRating[0], 2)
    co2DecimalRating = int(co2ScrubberRating[0], 2)
    print(o2DecimalRating*co2DecimalRating)
