# P1: 102 - ?
# P2: ? - ? 

DEBUG = True

DIRECTIONS = "NESW"
ARROWS2 = "^>v<"
ARROWS = "↑→↓←"
OFFSETS = [(0,-1), (1,0), (0,1), (-1,0)]

#POSITION, DIRECTION, STEP, VISITED, COST, PATH= 0, 1, 2,3,4,5
POSITION, DIRECTION, STEP, VISITED, COST, PATH= 'position', 'direction', 'step', 'visited', 'cost', 'path'


def main():
    
    print(f"Ex p1: {run('test.txt')}")

    #print(f"Ex p1: {run('example.txt')}")
    #print(f"In p1: {run('test.txt')}")
    #print(f"In p1: {run('input.txt')}")
    #print(f"Ex p2: {run('example.txt', 2)}")
    #print(f"In p2: {run('input.txt', 2)}")
    print("__")

def printMap(map, nodes = []):
    #print(nodes)
    positions = []
    for node in nodes:
        positions.append(node[POSITION])
    count = 0
    for y, row in enumerate(map):
        for x, c in enumerate(row):
            # if the row,c is in the nodes list, print it
            if (x, y) in positions:
                #positions.index(x, y)
                #node = nodes.find(lambda n: n[POSITION] == (x, y))
                #char = node[DIRECTION]
                print("x", end="")
            else:
                print(c, end="")
            if c == '#': 
                count+=1
        print()
    print(f"count = {count}")



def inRange(map, pos):
    return (pos[0] >= 0 and pos[0] < len(map[0]) and pos[1] >= 0 and pos[1] < len(map))


def getCost(map, visited):
    cost = 0
    for pos in visited:
        #print(pos)
        cost += int(map[pos[1]][pos[0]])
    return cost

def buildState(pos, direction = None, step = 0, visited = {}, cost = 0, path = []):
    state = {}
    state[POSITION] = pos
    state[DIRECTION] = direction
    state[STEP] = step
    state[VISITED] = visited
    state[COST] = cost
    state[PATH] = path
    return state
    
def printState(map, state, printPath = False):

    position = state[POSITION]
    step = state[STEP]
    #visited = state[VISITED]
    # direction = state[DIRECTION]
    cost = state[COST]
    path = state[PATH]
    endPosition = (len(map[0])-1, len(map)-1)
    md = manhattanDistance(position,endPosition)
    
    print(f"position = {position}, step = {step}, cost = {cost}, md = {md}")
    if printPath: print(f"path = {path}")

    mapCopy = []
    for row in map:
        rowCopy = row.copy()
        mapCopy.append(rowCopy)
        
    for s in path:
        pos = s[0]
        dir = s[1]
        mapCopy[pos[1]][pos[0]] = ARROWS[dir]
    if DEBUG: printMap(mapCopy)

def manhattanDistance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def run(filename, puzzlePart = 1):

    result = 0
        
    map = []

    for line in open(filename).read().splitlines():
        row = []
        for char in line:
            row.append(char)
        map.append(row)
 
    #printMap(map)

    if puzzlePart == 1:
        known = {}
        toVisit = []
        ns = buildState((0,0))
        toVisit.append(ns)
        

        maxRounds = 500000000
        minHeatLoss = 50000000
        minHeatLossPath = []

        reachedEnd = False
        round = 0
        while not reachedEnd:

            # stop search after a while since it's taking too long
            if maxRounds == 0:
                print(f"No solution found and len toVisit= {len(toVisit)}")
                break
            maxRounds -= 1
            round += 1

            newToVisit = []
            newToVisitStates = {}

            print(f"round = {round} with visitors = {len(toVisit)} and min = {minHeatLoss}")

            toVisitPositions = []
            for state in toVisit:
                toVisitPositions.append(state[POSITION])
            printMap(map, toVisit)
            
            if len(toVisit) == 0:
                print(f"No solution found and len toVisit= {len(toVisit)}")
                break
            
            for state in toVisit:
                # get a state
                state = toVisit.pop(0)            
                position = state[POSITION]
                step = state[STEP]
                visited = state[VISITED]
                direction = state[DIRECTION]
                #cost = getCost(map, visited)
                cost = state[COST]
                path = state[PATH]
    
                # check if we're in the finish position
                if position == (len(map[0])-1, len(map)-1):
                    if DEBUG: print(f"\n-------------> at end!!: cost={cost} nodes= {len(toVisit)}")
                    reachedEnd = True
                    if minHeatLoss < 0 or cost < minHeatLoss:
                        if DEBUG: print(f"new minHeatLoss: {cost}")    
                        path.append((position, direction))
                        if DEBUG: printState(map,state, True)
    
                        minHeatLoss = cost
                    continue
    
                # check if we're already over the minHeatLoss
                if minHeatLoss > 0 and cost > minHeatLoss:
                    if DEBUG: print(f"die: {position} {cost} {minHeatLoss}")
                    continue
                
                # check if we're in a known state with a higher cost
                key = (position, direction, step)
                if key in known and known[key] < cost:
                    #print(f"known: {key} {known[key]} < {cost}")
                    #continue
                    pass
                known[key] = cost
    
                # otherwise, spawn additional states
                validStates = []
                for newDirection in range(len(DIRECTIONS)):
     
                    offset = OFFSETS[newDirection]
                    newPosition = (position[0] + offset[0], position[1] + offset[1])
    
                    # don't go in reverse
                    if direction == ((newDirection + 2) % len(DIRECTIONS)):
                        continue
    
                    # don't take more than 3 steps in same direction
                    newStep = 0
                    if direction == newDirection:
                        newStep = step + 1
    
                    if newStep >= 3:
                        continue
    
                    # don't go off the map
                    if not inRange(map, newPosition):
                        continue
    
                    #if already visited, don't go there
                    if newPosition in visited:
                        continue
    
                    newVisited = visited.copy()
                    newVisited[newPosition] = True
                    
                    newPath = path.copy()
                    newPath.append((newPosition, newDirection))
                    
                    newCost = cost + int(map[newPosition[1]][newPosition[0]])
    
                    newState = buildState(newPosition, newDirection, newStep, newVisited, newCost, newPath)
    
                    validStates.append(newState)
    
                endPosition = (len(map[0])-1, len(map)-1)
                # sort the valid positions by the manhattan distance to the end
    
                #print("---\n")
                for state in validStates:
                    #printState(map, state)
                    pass
                
                validStates.sort(key=lambda state: manhattanDistance(state[POSITION],endPosition))
    
                validStates.sort(key=lambda state:state[COST])
                
                #print()
                for state in validStates:
                    #printState(map, state)
                    pass
                
    
                for newState in validStates:
                    #toVisit.insert(0,newState)
                    testPos = newState[POSITION]
                    testCost = newState[COST]*10 +newState[STEP]
                    
                    if testPos not in newToVisitStates:
                        newToVisitStates[testPos] = testCost
                        newToVisit.append(newState)
                    else:
                        if newToVisitStates[testPos] > testCost:
                            newToVisit.append(newState)
                            newToVisitStates[testPos] = testCost
                
                # the key is the position, step, and step
    
                
            
            #print(toVisit)
            toVisit = newToVisit
        return minHeatLoss
    elif puzzlePart == 2:
        pass
        
    return result


main()
