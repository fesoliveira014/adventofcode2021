def check_depth(measurements):
    numIncreases = 0
    for i in range(1, len(measurements)):
        if measurements[i-1] < measurements[i]:\
            numIncreases += 1
    return numIncreases

if __name__ == "__main__":
    measurements = []
    with open("input/01.txt", "r") as f:
        for line in f:
            measurements.append(int(line.strip("\n")))
    numIncreases = check_depth(measurements)
    print("number of increases: {}".format(numIncreases))
