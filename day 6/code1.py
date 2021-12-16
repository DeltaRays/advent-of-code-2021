class Sim:
    def __init__(self, fish: list[int]):
        self.fish = fish

    def step(self):
        fish = self.fish
        for i in range(len(self.fish)):
            if fish[i] == 0:
                fish.append(8)
                fish[i] = 7
            fish[i] -= 1


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
    data = [int(fish) for fish in raw_data.split(",")]
    simulation = Sim(data)

    for i in range(80):
        simulation.step()
    print("Total: {}".format(len(simulation.fish)))
