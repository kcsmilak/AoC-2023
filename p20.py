# P1: ? - 615127392 too low! --> 817896682
# P2: ? - ?

DEBUG = False
SIGNAME = ["low", "high"]


def main():
    #print(f"Ex p1: {run('test.txt')}")
    print(f"Ex1 p0: 0 ? {run('example.txt',0)}")
    print(f"Ex2 p0: 2 ? {run('example2.txt',0)}")
    print(f"Ex1 p1: 32000000 ? {run('example.txt', 1)}")
    print(f"Ex2 p1: 11687500 ? {run('example2.txt', 1)}")
    print(f"In p1: 817896682 ? {run('input.txt',1)}")
    #print(f"In p2: {run('input.txt', 2)}")
    print("__")


def run(filename, puzzlePart=1):

    result = 0

    modules = {}
    conjunctionRegistration = {}

    inputLines = open(filename).read().splitlines()
    for i, inputLine in enumerate(inputLines):
        type, name, value = None, None, None
        if inputLine.startswith("%") or inputLine.startswith("&"):
            type = inputLine[0]
            name = inputLine.split(" ")[0][1:].strip()
            value = 0
            pass
        elif inputLine.startswith("broadcaster"):
            type = "broadcaster"
            name = "broadcaster"
            pass
        else:
            raise Exception(f"Invalid input line {i}: {inputLine}")

        destinations = [s.strip() for s in inputLine.split("->")[1].split(",")]

        if type == "&":
            value = {}

        for destination in destinations:
            if not destination in modules:
                modules[destination] = ([], "destination", 0)
            #value[destination] = 0
            #if destination not in conjunctionRegistration:
            #    conjunctionRegistration[destination] = []
            #conjunctionRegistration[destination].append(name)

        #print(f"[{type}] [{name}] -> {destinations} : {value}")
        modules[name] = (destinations, type, value)

    # register the conjuction model inputs
    for moduleKey in modules:
        if modules[moduleKey][1] == "&":
            conjunctionRegistration[moduleKey] = []

    for moduleKey in modules:
        for destionation in modules[moduleKey][0]:
            if destionation in conjunctionRegistration:
                conjunctionRegistration[destionation].append(moduleKey)

    #print(conjunctionRegistration)

    #modules["output"] = ([], "output", 0)

    #print(modules)

    buttonPushes = 1 if puzzlePart == 0 else 1000
    lowPulses = 0
    highPulses = 0
    while buttonPushes > 0:
        buttonPushes -= 1
        lowPulses += 1

        pulses = []

        # a list of tulpes of destination, value (0 or 1), and source

        # spawn a pulse for each destination in the "broadcaster" module
        for destination in modules["broadcaster"][0]:
            pulses.append((destination, 0, "broadcaster"))
            lowPulses += 1

        # run the simulation
        maxRounds = 10000
        while True:
            if len(pulses) == 0:
                break

            if maxRounds <= 0:
                raise Exception("Too many rounds")
            maxRounds -= 1

            newPulses = []
            for pulse in pulses:

                name = pulse[0]
                pulseValue = pulse[1]
                source = pulse[2]

                module = modules[name]
                destinations = module[0]
                type = module[1]
                moduleValue = module[2]

                #print(f"CHECKING [{name}] [{type}] [{source}] -> {destinations} : {pulseValue} ")

                outputValue = None
                if "%" == type:
                    if pulseValue == 0:
                        moduleValue = (moduleValue + 1) % 2
                        modules[name] = (destinations, type, moduleValue)
                        outputValue = moduleValue



                elif "&" == type:

                    #print(f"source = {source} destination = {destination}")
                    #if source in destinations:
                    #    print(f"   [{name}] [{source}] -> {destinations} : {moduleValue}")
                    #    moduleValue[source] = pulseValue

                    outputValue = 1
                    for source in conjunctionRegistration[name]:
                        #print(f"checting {destination} with value {moduleValue[destination]}")
                        if modules[source][2] != 1:
                            outputValue = 0

                    #print(moduleValue)

                    outputValue = (outputValue + 1) % 2
                else:#if "output" == type:
                    #print("...")
                    moduleValue = moduleValue
                    modules[name] = (destinations, type, moduleValue)
                    outputValue = moduleValue

                    pass

                #else:
                #    raise Exception(f"Invalid type {type}")

                if outputValue is not None:



                    for destination in destinations:




                        if DEBUG: print(
                            f"\t\t[{source}] -[{SIGNAME[pulseValue]}]> \n{type}{name}  -{SIGNAME[outputValue]} -> {destination}"
                        )
                        if outputValue == 0:
                            lowPulses += 1
                        else:
                            highPulses += 1
                        newPulses.append((destination, outputValue, name))
                else:
                    #print(
                    #    f"  killing [{source}] -[{SIGNAME[pulseValue]}]> [{name}] {type}"
                    #)
                    pass

            pulses = newPulses

    if puzzlePart == 0:
        for module in modules:
            if "%" == modules[module][1]:
                result += modules[module][2]

    if puzzlePart == 1:
        print(f"lowPulses = {lowPulses} highPulses = {highPulses}")
        result = lowPulses * highPulses
    return result


main()
