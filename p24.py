# P1: 2 - =17776
# P2: ? - ?
P1E, P1I, P2E, P2I = 2, 17776, 47, None

import aoc_tools as aoc
DEBUG = False

def main():
    print(f"p1e: {run('p24.ex.txt',0)}")
    print(f"p1i: {run('p24.in.txt',1)}")
    print("__")


def parseInput(filename):
    positions, vectors = [], []
    for line in open(filename).read().splitlines():
        position = [ int(x) for x in line.split("@")[0].split(",") ]
        vector = [ int(x) for x in line.split("@")[1].split(",") ]
        positions.append(position)
        vectors.append(vector)
    return positions, vectors

def getEquation(position, vector):
    x0, y0 = position
    x1, y1 = position[0] + vector[0], position[1] + vector[1]

    m = (y1-y0)/(x1-x0)
    b = y0 - m*x0

    #print(f"y = {m}x + {b}")
    return m, b

def run(filename, puzzlePart = 1):
    answer = 0
    positions, vectors = parseInput(filename)

    x_min = 200000000000000
    x_max = 400000000000000
    y_min = 200000000000000
    y_max = 400000000000000

    if puzzlePart == 0:
        x_min = 7
        x_max = 27
        y_min = 7
        y_max = 27

    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            a = positions[i][0], positions[i][1]
            av = vectors[i][0], vectors[i][1]
            b = positions[j][0], positions[j][1]
            bv = vectors[j][0], vectors[j][1]

            am, ab = getEquation(a, av)
            bm, bb = getEquation(b, bv)

            a1 = Point(a[0], a[1])
            a2 = Point(a[0] + av[0], a[1] + av[1])

            b1 = Point(b[0], b[1])
            b2 = Point(b[0] + bv[0], b[1] + bv[1])

            result = lineLineIntersection(a1, a2, b1, b2)
            if None == result:
                #raise Exception("no intersection")
                pass
            else:
                intersection, determinate = result



                #print(f"intersection: {intersection}")
                if intersection[0] >= x_min and intersection[0] <= x_max and intersection[1] >= y_min and intersection[1] <= y_max:


                    # intersection.. but, are we looking forward or backward?
                    #TODO 


                    # is a headed towards the intersection or away?
                    adx = intersection[0] - a[0]
                    adx = adx / abs(adx)
                    ady = intersection[1] - a[1] 
                    ady = ady / abs(ady)

                    if adx == av[0]/abs(av[0]) and ady == av[1]/abs(av[1]):
                        # a is heading towards the intersection

                        #DO sometihng

                        # is the other headed towards the intersection or away?
                        bdx = intersection[0] - b[0]
                        bdx = bdx / abs(bdx)
                        bdy = intersection[1] - b[1]
                        bdy = bdy / abs(bdy)

                        if bdx == bv[0]/abs(bv[0]) and bdy == bv[1]/abs(bv[1]):
                            # b is heading towards the intersection
                            #print(f"{positions[i]} x {positions[j]} --> {intersection} {determinate}  adx: {adx} ady: {ady} avx: {av[0]/abs(av[0])} avy: {av[1]/abs(av[1])}")
                            answer += 1


    return answer


# Python program to find the point of
# intersection of two lines

# Class used to used to store the X and Y
# coordinates of a point respectively
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Method used to display X and Y coordinates
    # of a point
    def displayPoint(self, p):
        print(f"({p.x}, {p.y})")

    def __str__(self):
        return f"({self.x}, {self.y})"


def lineLineIntersection(A, B, C, D):
    # Line AB represented as a1x + b1y = c1
    a1 = B.y - A.y
    b1 = A.x - B.x
    c1 = a1*(A.x) + b1*(A.y)

    # Line CD represented as a2x + b2y = c2
    a2 = D.y - C.y
    b2 = C.x - D.x
    c2 = a2*(C.x) + b2*(C.y)

    determinant = a1*b2 - a2*b1

    if (determinant == 0):
        return None
    else:
        x = (b2*c1 - b1*c2)/determinant
        y = (a1*c2 - a2*c1)/determinant
        return (x,y), determinant
