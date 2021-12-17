if __name__ == "__main__":
    with open("input.txt") as file:
        raw_input_data = file.read()
    with open("example.txt") as file:
        raw_example_data = file.read()

    # A variable used to choose which one of the two to use
    # Example data is used to see if the code works
    use_example_data = True

    if use_example_data:
        raw_data = raw_example_data
    else:
        raw_data = raw_input_data
    lines = raw_data.split("\n")
    possible_segments = [c for c in "abcdefg"]
    for line in lines:
        corrispondence = {
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: None,
            7: None,
            8: None,
            9: None
        }
        first_part, second_part = line.split(" | ", 2)
        inpt: list[str] = first_part.split(" ")
        output: list[str] = second_part.split(" ")
        # Loop to find which segments correspond to what
        for word in inpt:
            # 2, 3, 4, 7 are the number of different segments for 1, 4, 7, 8
            #                                                     2, 4, 3, 7
            # Lengths: 1 2 3 4 5 6 7 8 9 0
            #          2 5 5 4 5 6 3 7 6 6
            if len(word) == 2:
                corrispondence[1] = word
                inpt.remove(word)
            elif len(word) == 4:
                corrispondence[4] = word
                inpt.remove(word)
            elif len(word) == 3:
                corrispondence[7] = word
                inpt.remove(word)
            elif len(word) == 7:
                corrispondence[8] = word
                inpt.remove(word)
        for word in inpt:
            if len(word) == 5 and len(set([c for c in word] + [c for c in corrispondence[1]])) == 5:
                corrispondence[3] = word
                inpt.remove(word)
        top_right_segment: str = ""
        for word in inpt:
            if len(word) == 6:
                # If it's a 6 this means that it doesn't have only a segment 1 does (this also lets us afterwards get
                # 2 and 5
                chars_in_1_in_6 = [char not in word for char in corrispondence[1]]
                if any(chars_in_1_in_6):
                    corrispondence[6] = word
                    top_right_segment = [i for (v, i) in enumerate(corrispondence[1]) if chars_in_1_in_6[v]][0]
        for word in inpt:
            if len(word) ==5 and word.__contains__()

        print(corrispondence)
