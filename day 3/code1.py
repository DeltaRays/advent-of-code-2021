with open("input.txt") as f:
    raw = f.read()
    array = raw.split("\n")
    length = len(array)

    bit1Count = [0] * len(array[0])


    for i in array:
        for j in range(len(i)):
            bit1Count[j] += int(i[j])
    print(length)

    gamma = [''] * len(bit1Count)
    epsilon = [''] * len(bit1Count)
    for i in range(len(bit1Count)):
        if (bit1Count[i] / length) >= 0.5:
            gamma[i] = '1'
            epsilon[i] = '0'
        else:
            gamma[i] = '0'
            epsilon[i] = '1'

    gammaBinary = "".join(gamma)
    epsilonBinary = "".join(epsilon)

    gammaDecimal = int(gammaBinary, 2)

    epsilonDecimal = int(epsilonBinary, 2)

    print("Power consumption: {}".format(epsilonDecimal * gammaDecimal))
