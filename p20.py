# P1: ? - 
# P2: ? - v615127392 =817896682
# lowPulses = 18266 highPulses = 44777

DEBUG = False
SIGNAME = ["low", "high"]


P1E, P1I, P2E, P2I = 11687500, 817896682, None, None

def main():
    #print(f"Ex p1: {run('test.txt')}")
    #print(f"Ex1 p0: 0 ? {run('example.txt',0)}")
    #print(f"Ex2 p0: 2 ? {run('example2.txt',0)}")
    #print(f"Ex1 p1: 32000000 ? {run('example.txt', 1)}")
    #print(f"Ex2 p1: 11687500 ? {run('example2.txt', 1)}")
    #print(f"In p1: 817896682 ? {run('input.txt',1)}")
    print(f"In p1: 817896682 ? {run('input.txt',2)}")
    #print(f"In p2: {run('input.txt', 2)}")
    print("__")


def run(filename, puzzlePart=1):

    if puzzlePart == 2 and filename == "p20.ex.txt": return None

    result = 0

    modules = {}
    conjunctionRegistration = {}

    inputLines = open(filename).read().splitlines()
    for i, inputLine in enumerate(inputLines):
        type, name, value = None, None, None

        if inputLine.startswith("%") or inputLine.startswith("&"):
            type = inputLine[0]
            name = inputLine.split(" ")[0][1:].strip()
            value = 0 if type == "%" else {}
            pass
        elif inputLine.startswith("broadcaster"):
            type = "broadcaster"
            name = "broadcaster"
            pass
        else:
            raise Exception(f"Invalid input line {i}: {inputLine}")

        destinations = [s.strip() for s in inputLine.split("->")[1].split(",")]

        #print(f"[{type}] [{name}] -> {destinations} : {value}")
        modules[name] = (destinations, type, value, {})

    # register the conjuction model inputs
    for moduleKey in modules:
        if modules[moduleKey][1] == "&":
            conjunctionRegistration[moduleKey] = []

    for moduleKey in modules:
        for destination in modules[moduleKey][0]:
            if destination in conjunctionRegistration:
                conjunctionRegistration[destination].append(moduleKey)
            else:
                conjunctionRegistration[destination] = [moduleKey]

    buttonPushes = 0
    maxButtonPushes = 1
    if puzzlePart == 1:
        maxButtonPushes = 1000
    else:
        maxButtonPushes = 100000000
    lowPulses, highPulses = 0, 0
    for _ in range(maxButtonPushes):

        if buttonPushes % 10000 == 0: print(".", end="", flush=True)

        buttonPushes += 1
        lowPulses += 1

        pulses = []
        # spawn a pulse for each destination in the "broadcaster" module
        for destination in modules["broadcaster"][0]:
            pulses.append((destination, 0, "broadcaster"))

        # run the simulation
        rxPushes = 0
        while pulses:
            name, pulseValue, source = pulses.pop(0)

            if pulseValue == 0:
                lowPulses += 1
                if "rx" == name:
                    rxPushes += 1
                    print("rxPushes", rxPushes)
            else:
                highPulses += 1

            if not name in modules:
                continue

            destinations, type, moduleValue, conjunctionMemory = modules[name]
            #print(f"CHECKING [{name}] [{type}] [{source}] -> {destinations} : {pulseValue} ")

            outputValue = None

            if "%" == type:
                if pulseValue == 0:
                    moduleValue = (moduleValue + 1) % 2
                    modules[name] = (destinations, type, moduleValue, conjunctionMemory)
                    outputValue = moduleValue

            elif "&" == type:

                conjunctionMemory[source] = pulseValue

                outputValue = 1
                for source in conjunctionRegistration[name]:
                    val = None
                    if not source in conjunctionMemory:
                        val = 0
                    else:
                        val = conjunctionMemory[source]

                    if val == 0:
                        outputValue = 0

                modules[name] = (destinations, type, moduleValue, conjunctionMemory)

                #print(moduleValue)

                outputValue = (outputValue + 1) % 2
            elif "broadcaster" == type:
               raise Exception("BROADCASTER") 
            else:
                outputValue = moduleValue

            if outputValue is not None:

                for destination in destinations:

                    if DEBUG: print(
                        f"\t\t[{source}] -[{SIGNAME[pulseValue]}]> \n{type}{name}  -{SIGNAME[outputValue]} -> {destination}"
                    )

                    pulses.append((destination, outputValue, name))
            else:
                #print(
                #    f"  killing [{source}] -[{SIGNAME[pulseValue]}]> [{name}] {type}"
                #)
                pass
        if rxPushes == 1:
            print(f"breaking because single rx push at round {buttonPushes}")
            break

    if puzzlePart == 0:
        for module in modules:
            if "%" == modules[module][1]:
                result += modules[module][2]

    if puzzlePart == 1:
        #print(f"lowPulses = {lowPulses} highPulses = {highPulses}")
        result = lowPulses * highPulses

    if puzzlePart == 2:
        print(f"buttonPushes = {buttonPushes}")
        result = buttonPushes
    return result

