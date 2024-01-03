# P1: ? - ?
# P2: ? - ? 

DEBUG = True

DIRECTIONS = "NESW"
ARROWS2 = "^>v<"
ARROWS = "↑→↓←"
OFFSETS = [(0,-1), (1,0), (0,1), (-1,0)]

#POSITION, DIRECTION, STEP, VISITED, COST, PATH= 0, 1, 2,3,4,5
POSITION, DIRECTION, STEP, VISITED, COST, PATH= 'position', 'direction', 'step', 'visited', 'cost', 'path'


def printMap(map):
    print()
    count = 0
    for row in map:
        print(''.join(row))
        for c in row:
            if c == '#': count+=1
    #print(f"count = {count}")

def inRange(map, pos):
    return (pos[0] >= 0 and pos[0] < len(map[0]) and pos[1] >= 0 and pos[1] < len(map))

#destinations = [s.strip() for s in inputLine.split("->")[1].split(",")]

#map = [[0 for column in width] for row in height]
