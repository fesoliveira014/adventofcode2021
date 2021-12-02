def check_depth(measurements):
    prevSum = 0
    numIncreases = 0
    for i in range(0, len(measurements)):
        if (i + 1) >= len(measurements) or (i + 2) >= len(measurements):
            break
        currSum = measurements[i] + measurements[i+1] + measurements[i+2]
        if prevSum != 0 and currSum > prevSum:
            numIncreases += 1
        prevSum = currSum
    return numIncreases

if __name__ == "__main__":
    measurements = []
    with open("input/02.txt", "r") as f:
        for line in f:
           measurements.append(int(line.strip("\n")))
    numIncreases = check_depth(measurements)
    print("number of increases: {}".format(numIncreases))