# P1: ? - ?
# P2: ? - ?

import aoc_tools as aoc
DEBUG = False

def main():
    print(f"p1e: {run('p23.ex.txt')}")
    #print(f"p2e: {run('p23.ex.txt',2)}")
    #print(f"p1i: {run('p23.in.txt')}")
    print(f"p1i: {run('p23.in.txt',2)}")

    print("__")



def run(filename, puzzlePart = 1):

    # global memory is [position, visited, direction] = steps


    grid = aoc.buildMapFromFile(filename)
    if DEBUG: aoc.printMap(grid)

    start = (1, 0)
    end = (len(grid[0])-2, len(grid)-1)

    #grid[start[1]][start[0]] = 'S'
    #grid[end[1]][end[0]] = 'E'

    positionBest = {}


    longestPath = []
    states = []
    # a state is the position, direction, step, path
    states.append((start, '2' , [(start)]))

    maxRounds = 100000000
    while len(states) > 0:
        maxRounds -= 1
        if maxRounds == 0: raise Exception("maxRounds")

        state = states.pop()
        position, direction, path = state

        # if we're at the end and longest path, remember that
        if position == end:
            if len(path) > len(longestPath):
                longestPath = path.copy()
                print(f"longestPath: {len(longestPath)-1}")
            continue


        # skip if not the best at this position
        if puzzlePart == 2:
            visitedString = aoc.visitedString(path)
            memoryKey = (position, direction, visitedString)
            if memoryKey in positionBest:
                if positionBest[memoryKey] < len(path):
                    print(f"killing: {memoryKey}")
                    continue
            else:
                positionBest[memoryKey] = len(path)

        # check for each possible step we can take
        for step in range(len(aoc.DIRECTIONS)):

            valid = False

            newPosition = (position[0] + aoc.OFFSETS[step][0], position[1] + aoc.OFFSETS[step][1])

            # skip anything not in the grid
            if not aoc.inRange(grid, newPosition):
                continue

            # skip places we've already been
            if newPosition in path:
                continue

            newTile = grid[newPosition[1]][newPosition[0]]

            # skip if hitting a wall
            if newTile == '#':
                continue

            # skip if going the wrong way
            if newTile in aoc.ARROWS_PLAIN:
                arrow = aoc.ARROWS_PLAIN[step]
                if arrow == newTile:
                    valid = True
                else:
                    if puzzlePart == 1:
                        # wrong way!
                        continue
                    else:
                        valid = True

            # allow moving if a space
            if newTile == '.':
                valid = True

            if not valid:
                raise Exception("unknown tile")

            if DEBUG: print(f"adding {newPosition} {direction} {step} {path}")
            newPath = path.copy()
            newPath.append(newPosition)
            states.append((newPosition, direction, newPath))


    return len(longestPath)-1

