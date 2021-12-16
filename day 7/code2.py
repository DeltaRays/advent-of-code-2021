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
    parsed_data = [int(dist) for dist in raw_data.split(",")]


    def fuel_cost_from_dist(x: int) -> int:
        # Using int() only because otherwise the compiler warns about type (but we know for sure that x*(x+1)/2 if x
        # is an integer will be an int, no matter the number.
        return int(x * (x + 1) / 2)


    value = min([sum([fuel_cost_from_dist(abs(v - x)) for x in parsed_data]) for v in range(len(parsed_data))])
    print(f"Answer: {value}")
