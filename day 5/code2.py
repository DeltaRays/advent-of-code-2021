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
    lines = [[tuple(int(coord) for coord in segment.split(",")) for segment in line.split(" -> ")] for line in
             raw_data.split("\n")]
    points = []
    print(lines)
    for line in lines:
        point1 = line[0]
        point2 = line[1]

        # Here we can't simply use min() and max() because order matters
        x_sign = 1 if (point2[0] > point1[0]) else -1
        y_sign = 1 if (point2[1] > point1[1]) else -1

        x_range = range(point1[0], point2[0] + x_sign, x_sign)
        y_range = range(point1[1], point2[1] + y_sign, y_sign)

        if point1[0] == point2[0]:
            points.extend([(point1[0], y) for y in y_range])
        elif point1[1] == point2[1]:
            points.extend([(x, point1[1]) for x in x_range])
        else:
            points.extend(list(zip(x_range, y_range)))

    count = collections.Counter(points)
    intersections = [point for point in count.values() if point > 1]
    print("Answer: {}".format(len(intersections)))
