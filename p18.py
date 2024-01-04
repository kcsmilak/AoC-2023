# P1: 62 - 52055
# P2: 952408144115 - ? 

P1E = 62
P1I = 52055
P2E = 952408144115
P2I = None

DEBUG = False

DIRECTIONS = "NESW"
MOVEMENTS = "URDL"
ARROWS2 = "^>v<"
ARROWS = "↑→↓←"
OFFSETS = [(0,-1), (1,0), (0,1), (-1,0)]

X = 0
Y = 1

def main():
    
    #print(f"Te p1: {run('test.txt')}")
    #print(f"Te p2: {run('test.txt',2)}")

    #print(f"Ex p1: {run('example.txt')}")
    #print(f"Ex p1: {run('example.txt',2)}")

    print(f"In p1: {run('18.in')}")
    #print(f"Ex p2: {run('test.txt', 2)}")
    #print(f"In p2: {run('input.txt', 2)}")
    print("_x")

def printMap(map):
    print()
    count = 0
    for row in map:
        #print(''.join(row))
        for c in row:
            print(c[0], end='')
            if c[0] == '#': count+=1
        print()
    print(f"\ncount = {count}")

def countSymbol(map, symbol):
    count = 0
    for row in map:
        for c in row:
            if c[0] == symbol: count+=1
    return count

def buildMap(width, height):
    map = []
    for i in range(height):
        map.append(['.'] * width)
    return map

def inRange(map, pos):
    return (pos[0] >= 0 and pos[0] < len(map[0]) and pos[1] >= 0 and pos[1] < len(map))

def expandMap(map, movement, size = 1):
    if "U" == movement:
        for i in range(size):
            map.insert(0, ['.'] * len(map[0]))
    elif "D" == movement:
        for i in range(size):
            map.append(['.'] * len(map[0]))
        pass
    elif "D" == movement:
        pass
    else:
        for row in map:
            if "R" == movement:
                row.append('.' * size)
            elif "L" == movement:
                row.insert(0, "." * size)
            else:
                raise Exception(f"Unknown movement: {movement}")

def fillMap(map, edges):
    for edge in edges:
        x = edge[0] + 1
        y = edge[1]
        while inRange(map, (x,y)) and map[y][x] == '.':
            map[y][x] = '#'
            x += 1

def run(filename, puzzlePart = 1):

    result = 0
        
    instructions = []
    map = [['.']]


    for line in open(filename).read().splitlines():
        movement = line.split()[0].strip()
        steps = int(line.split()[1])
        color = line.split()[2][1:-1]
        instructions.append((movement, steps, color))

    #print(instructions)


    if puzzlePart == 1:


        maxX = 0
        minX = 0
        maxY = 0
        minY = 0
        x = 0
        y = 0

        edges = []
        
        for instruction in instructions:

            if DEBUG: print(instruction)
            movement = instruction[0]
            steps = instruction[1]
            color = instruction[2]

            if movement == "U": y -= steps
            elif movement == "D": y += steps
            elif movement == "L": x -= steps
            elif movement == "R": x += steps
            else:
                raise Exception(f"Unknown movement: {movement}")

            if x < minX: minX = x
            if x > maxX: maxX = x
            if y < minY: minY = y
            if y > maxY: maxY = y

        if DEBUG: print(f"minX = {minX}, maxX = {maxX}, minY = {minY}, maxY = {maxY}")

        width = maxX - minX + 1
        height = maxY - minY + 1


        if DEBUG: print(f"width = {width}, height = {height}")
        map = buildMap(width, height)
        
        if DEBUG: printMap(map)

        x = -minX
        y = -minY

        for instruction in instructions:
            movement = instruction[0]
            steps = instruction[1]
            color = instruction[2]

            offset = OFFSETS[MOVEMENTS.index(movement)]

            for i in range(steps):
                map[y][x] = ARROWS[MOVEMENTS.index(movement)]
                x += offset[0]
                y += offset[1]
            
            #x = x + offset[0] * steps
            #y = y + offset[1] * steps

        if DEBUG: printMap(map)

        for y, row in enumerate(map):
            for x, c in enumerate(row):
                if c == ARROWS[0]:# or c == ARROWS[3]:
                    edges.append((x,y))
                    edges.append((x,y-1))
        

        fillMap(map, edges)

        for y, row in enumerate(map):
            for x, c in enumerate(row):
                if c != ".":
                    map[y][x] = '#'


        
        if DEBUG: printMap(map)
        
        result = countSymbol(map, '#')
    elif puzzlePart == 2:

        #print("PART 2")

        points = []
        rowTransitions = {}

        x, y = 0, 0
        minX, minY = 0, 0
        maxX, maxY = 0, 0
        
        for instruction in instructions:

            #print(f"x = {x}, y = {y}")
            points.append((x,y))

            #print(instruction)
            movement = instruction[0]
            steps = instruction[1]
            color = instruction[2]
            
            offset = OFFSETS[MOVEMENTS.index(movement)]


            if x < minX: minX = x
            if x > maxX: maxX = x
            if y < minY: minY = y
            if y > maxY: maxY = y

            if offset[Y] == 0:
                val = (x, x+steps) if offset[X] > 0 else (x-steps, x)
                if y in rowTransitions:
                    rowTransitions[y].append(val)
                else:
                    rowTransitions[y] = [val]

            else:
                # for every row we cross, add this item
                pass
            
            
            x = x + offset[0] * steps
            y = y + offset[1] * steps

        #print(f"rowTransitions = {rowTransitions}")
        #points.append((x,y))

        temp = 0
        points.reverse()
        # adjust all points into right quadrant
        newPoints = []
        for p in points:
            #print(p)
            px = p[X] + abs(minX) + 1
            py = p[Y] + abs(minY) + 1
        newPoints.append((px,py))

        
        #points = newPoints
        #print(points)
        for i, point in enumerate(points):

            pointA = points[i]
            pointB = points[i+1] if i+1 < len(points) else points[0]

            # get the determinate of pointA and pointB
            det = abs((pointA[X] * pointB[Y]) - (pointB[X] * pointA[Y]))
            #print(f"pointA = {pointA}, pointB = {pointB} det = {det}")

            result += det 
            temp += det // 2
            
        #print(temp)

        result = Area(points)
    return result

def Area(corners):
    n = len(corners) # of corners
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area

# (X[i], Y[i]) are coordinates of i'th point.
def polygonArea(points):
    n = len(points)
    
    
    # Initialize area
    area = 0.0

    # Calculate value of shoelace formula
    j = n - 1
    for i in range(0,n):
        area += (points[j][0] + points[i][0]) * (points[j][1] - points[i][1])
        j = i   # j is previous vertex to i


    # Return absolute value
    return int(abs(area / 2.0))

"""
Provides a way to caculate the area of an arbitrary
n-sided irregular polygon.
"""
import doctest
import math

def heron(a,b,c):
    """
    Uses the heron formula to calculate the area
    of the triangle where `a`,`b` and `c` are the side
    lengths.

    >>> heron(3, 4, 5)
    6.0
    >>> heron(7, 10, 5).__round__(2)
    16.25
    """
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def pytagoras(a, b):
    """
    Given the cathets finds the hypotenusas.

    >>> pytagoras(3, 4)
    5.0
    """
    return math.sqrt(a**2 + b**2)

def distance(point_1, point_2):
    """
    Computes the cartesian distance between two points.

    >>> distance((0,0), (5,0))
    5.0
    """
    delta_x = point_1[0] - point_2[0]
    delta_y = point_1[1] - point_2[1]
    return pytagoras(delta_x, delta_y)

def triangle_area(triangle):
    """
    Wraps `heron` by allowing points inputs instead
    of sides lengths inputs.

    >>> triangle_area([(0,0), (0,3), (4,0)])
    6.0
    """
    side_1 = distance(triangle[0], triangle[1])
    side_2 = distance(triangle[1], triangle[2])
    side_3 = distance(triangle[2], triangle[0])
    return heron(side_1, side_2, side_3)

def triplets(list_):
    """
    Yields items from a list in groups of 3.

    >>> list(triplets(range(6)))
    [(0, 1, 2), (1, 2, 3), (2, 3, 4), (3, 4, 5)]
    """
    for index, item in enumerate(list_[:-2]):
        yield item, list_[index + 1], list_[index + 2]

def polygon_area(polygon):
    """
    Calculates the area of an n-sided polygon by
    decomposing it into triangles. Input must be
    a list of points.

    >>> polygon_area([(0,0), (0,5), (3,0), (3, 5)])
    15.0
    """
    return sum(triangle_area(triangle)
                   for triangle in triplets(polygon))




