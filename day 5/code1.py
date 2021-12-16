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
    data = [[tuple(int(coord) for coord in segment.split(",")) for segment in line.split(" -> ")] for line in
            raw_data.split("\n")]
    straight_lines = [line for line in data if line[0][0] == line[1][0] or line[0][1] == line[1][1]]
    points = []
    for line in straight_lines:
        point1 = line[0]
        point2 = line[1]
        for x in range(min(point1[0], point2[0]), max(point1[0], point2[0]) + 1):
            for y in range(min(point1[1], point2[1]), max(point1[1], point2[1]) + 1):
                points.append((x, y))
    count = collections.Counter(points)
    intersections = [point for point in count.values() if point > 1]
    print("Answer: {}".format(len(intersections)))
