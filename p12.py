# P1: ? - too high 6841 (should be 6488)
# P2: ? - ? (should be 815364548481)

DEBUG = False
lineTest = -1



def main():
    #print(f"Ex p1: {run('example.txt')}")
    #print(f"Ex p2: {run('example.txt',2)}")
    #print(f"In p1: {run('input.txt')}")
    print(f"In p2: {run('p12.in.txt', 2)}")
    print("__")


# the amount of space until either a # or the end of the line
def spaceAhead(line, offset=0):
    position = offset
    space = 0
    while True:
        if position >= len(line) or line[position] == '.':
            break
        space += 1
        position += 1
    return space


def leakAllowed(line, leakSize):
    #print(f"leakAllowed: {line}, {leakSize}")
    offset = 0

    for i in range(leakSize):
        if i >= len(line):
            return False
        if line[i] == '#':
            continue
        if line[i] == '.':
            return False
        if line[i] == '?':
            continue

    if leakSize == len(line):
        return True

    if line[leakSize] == '#':
        return False
    if line[leakSize] == '.':
        return True
    if line[leakSize] == '?':
        return True

    
    return
    
    while True:
        if offset == len(line):
            break
        if line[offset] == '.':
            break
        if offset == leakSize:
            if offset + 1 == len(line):
                return True
            if line[offset+1] == '.':
                return True
            if line[offset+1] == '?':
                return True
            return False
        offset += 1
    return False

    


def placeLeaks2(line, leaks):

    leakSum = sum(leaks)
    minSpace = len(leaks) - 1 + leakSum
    print(f"minSpace: {minSpace}")  # optimization for later

    print(f"line: {line} leaks: {leaks} minSpace: {minSpace}")

    for i in range(len(line)):

        # first try to use the space

        space = spaceAhead(line, i)
        remainingLeaks = leaks[offset + 1:]
        print(f"space={space}  len={len(line)} offset = {offset}")

        remainingLine = line[i + 2:]
        placeLeaks(remainingLine, remainingLeaks)

        # now advance to the next place without using the space

    return

    placedLeaks = 0
    for i in range(len(line)):
        if line[i] == ".":
            continue
        else:
            if len(remainingLeaks) > 0: placeLeaks(line[i:], remainingLeaks)
            break

    return


def placeLeaks(line, leaks):
    """
    For each valid position, place the first leak in the line, then recrusively
    call to place the remaining leaks.
    """

    if DEBUG: print(f"line: {line:>20}    l: {leaks}")

    combinations = 0

    if len(leaks) == 0:

        # make sure there are no #s left
        if "#" in line:
            return 0
        
        #print("found valid")
        return 1 # this was a valid outcome
    if len(line) == 0 and len(leaks) > 0:
        return 0
    
    leakSize = leaks[0]
    remainingLeaks = leaks[1:]

    if line[0] == "#":
        # we *must* place the leak and then split line and continue *if*
        # there is enough space to consume the leak

        if leakAllowed(line,leakSize):
        
            return placeLeaks(line[leakSize+1:], remainingLeaks)
        else:
            #print(f"can't place leak {leakSize} in {line}")
            return 0

    if line[0] == ".":
        # we *must* skip the position
        return placeLeaks(line[1:], leaks)

    # since it's a ?, we can either use the space as a . or as a #,
    # only use as a # *if* there is actually enough space to consume 
    # the leak

    # TODO

    # always send off assuming we'd a '.'
    combinations += placeLeaks(line[1:], leaks)

    if leakAllowed(line, leakSize):
        combinations += placeLeaks(line[leakSize+1:], remainingLeaks)
    else:
        #print(f"can't place leak {leakSize} in {line}")
        pass

    return combinations
    # now *try* to place the leak first available position
    offset = 0
    while True:
        print(f"offset: {offset}, line {line}")
        if offset == len(line) or line[offset + 1] == '.' or line[offset + 1] == '?':
            combinations += placeLeaks(line[offset + 2:], remainingLeaks)
        offset += 1
        if offset >= len(line):
            break

    return combinations
    
    space = spaceAhead(line, offset)
    print(f"offset: {offset}  leakSize: {leakSize}  space: {space}")
    if leakSize <= space or (leakSize == space and offset+space == len(line)):
        # place the leak
        remainingLine = line[offset + leakSize + 1:]
        # place the remaining leaks
        placeLeaks(remainingLine, remainingLeaks)

        # also *don't* place the leak
        #remainingLine = line[offset + 1:]
        #placeLeaks(remainingLine, leaks)
    
        
            
        


def getArrangementsCount(line, leaks):
    arrangements = 0

    # create each possible right, and see if that fits into left

    arrangements = placeLeaks(line, leaks)

    print(f"{line:20} {leaks} -> {arrangements}")
    return arrangements


def run(filename, puzzlePart=1):

    result = 0

    inputLines = open(filename).read().splitlines()
    for i, inputLine in enumerate(inputLines):
        line = inputLine.split(" ")[0]
        leaks = [int(x) for x in inputLine.split(" ")[1].split(",")]
        
        
        

        if puzzlePart == 2:
            oLine = line
            oLeaks = leaks.copy()
            for i in range(4):
                line = line + "?" + oLine 
                for j in range(len(oLeaks)):
                    leaks.append(oLeaks[j])

        #print(line)
        #print(leaks)
            
        if lineTest == -1 or lineTest == i:
            result += getArrangementsCount(line, leaks)

                
        

    return result


main()


"""

if #, 
  if enough space
    return placeRemainder using block
  else
    invalid option
    return 0

if .
  return placeRemainder

if ?
  if enough space
    a = placeRemainder using block
  
   b = placeRemainder
   return a + b
   


"""
