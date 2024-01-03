# P1: 142 -- 54632
# P2: 281 -- 54019

P1E = 142
P1I = 54632
P2E = 281
P2I = 54019

PART1, PART2, EXAMPLE, INPUT, DEBUG = True, True, True, True, False

textNumbers = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}

def run(filename, allowWords = False):
    fullTotal = 0

    for line in open(filename).read().splitlines():
        firstNumber = None
        secondNumber = None
        buffer = ""
        for char in line:
            val = None
            if ord(char) >= ord("0") and ord(char) <= ord("9"):
                val = int(char)
                buffer = ""
            elif allowWords:
                buffer += char

                left = len(buffer) - min(len(buffer), 5)
                subbuffer = buffer[left:len(buffer)]

                for key in textNumbers.keys():
                    if key in subbuffer:
                       val = textNumbers[key]
            if val is not None:
                if firstNumber is None:
                    firstNumber = val
                    secondNumber = val
                else:
                    secondNumber = val
        if (DEBUG): print(f"{line} -> {firstNumber}:{secondNumber}")
        fullTotal += firstNumber * 10 + secondNumber
    return fullTotal
