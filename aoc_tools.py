# P1: ? - ?
# P2: ? - ? 

DEBUG = True

DIRECTIONS = "NESW"
ARROWS_PLAIN = "^>v<"
ARROWS = "↑→↓←"
OFFSETS = [(0,-1), (1,0), (0,1), (-1,0)]

#POSITION, DIRECTION, STEP, VISITED, COST, PATH= 0, 1, 2,3,4,5
POSITION, DIRECTION, STEP, VISITED, COST, PATH= 'position', 'direction', 'step', 'visited', 'cost', 'path'

def buildMapFromFile(filename):
    grid = []
    for line in open(filename).read().splitlines():
        row = [ x for x in line]
        grid.append(row)
    return grid

def printMap(map, path = None):
    print()
    count = 0
    for y,row in enumerate(map):
        for x,c in enumerate(row):
            if path is not None and (x,y) in path:
                print(ARROWS_PLAIN[path[(x,y)]], end="")
            else:
                print(c, end="")
            if c == '#': count+=1
        print()
    print(f"count = {count}")

def inRange(map, pos):
    return (pos[0] >= 0 and pos[0] < len(map[0]) and pos[1] >= 0 and pos[1] < len(map))

#destinations = [s.strip() for s in inputLine.split("->")[1].split(",")]

#map = [[0 for column in width] for row in height]

def pathString(path):
    str = ""
    for position in path:
        str += f"({position[0]},{position[1]}),"
    str = str[:-1]
    return str

def visitedString(path):
    path = path.copy()
    path.sort()
    return pathString(path)
