import collections

if __name__ == "__main__":
    with open("input.txt") as file:
        raw_input_data = file.read()
    with open("example.txt") as file:
        raw_example_data = file.read()

    # A variable used to choose which one of the two to use
    # Example data is used to see if the code works
    use_example_data = False

    if use_example_data:
        raw_data = raw_example_data
    else:
        raw_data = raw_input_data

    data = [int(i) for i in raw_data.split(",")]

    # We need to use another method from the last one since 256 is too much
    # I ended up figuring out a better way to do it, that is saving the number of fish that are in each stage
    lifes = collections.Counter(data)
    for i in range(256):
        lifes = {l: 0 if lifes.get(l + 1) is None else lifes.get(l + 1) for l in range(-1, 8)}
        lifes[8] = lifes[-1]
        lifes[6] += lifes[-1]
        lifes[-1] = 0
    print("Answer: {}".format(sum(lifes.values())))
