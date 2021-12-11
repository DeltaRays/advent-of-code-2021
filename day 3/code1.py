with open("input.txt") as f:
    raw = f.read()
    array = raw.split("\n")
    length = len(array)

    data = [0] * len(array[0])

    print(len(data))

    for i in array:
        for j in range(len(i)):
            data[j] += int(i[j])
    print(length)

    gamma = [''] * len(data)
    epsilon = [''] * len(data)
    for i in range(len(data)):
        if (data[i] / length) >= 0.5:
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
