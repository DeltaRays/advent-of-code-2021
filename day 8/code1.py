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
    parsed_data = raw_data.split("\n")
    data_we_care_about = [line.split(" | ")[-1].strip().split() for line in parsed_data]
    flattened_data = [word for sublist in data_we_care_about for word in sublist]
    # 2, 3, 4, 7 are the number of different segments for 1, 4, 7, 8
    #                                                     2, 4, 3, 7
    print(f"Total: {len([word for word in flattened_data if len(word) in (2, 3, 4, 7)])}")
