# P1: ? - ?
# P2: ? - ?
P1E, P1I, P2E, P2I = 5, 434, 7, None

import aoc_tools as aoc
DEBUG = False
DAY = "22"

def main():
    print(f"p1e: {run('p' + DAY + '.ex.txt')}")
    #print(f"p2e: {run('p' + DAY + '.ex.txt',2)}")
    print(f"p1i: {run('p' + DAY + '.in.txt')}")
    #print(f"p1i: {run('p' + DAY + '.in.txt',2)}")

    print("__")


def printGrid(grid):
    for row in grid:
        for cell in row:
            if cell == -1:
                print(f"  •" , end="")
            else:
                print(f"{cell:3}", end="")
        print("")
    print()


def run(filename, puzzlePart = 1):
    result = 0

    bricks = []
    inputLines = open(filename).read().splitlines()
    x_min = 0
    x_max = 0
    y_min = 0
    y_max = 0
    z_min = 0
    z_max = 0

    for line in inputLines:
        p0 = [int(x) for x in line.split("~")[0].split(",")]
        p1 = [int(x) for x in line.split("~")[1].split(",")]

        if p0[0] > x_max: x_max = p0[0]
        if p1[0] > x_max: x_max = p1[0]
        if p0[1] > y_max: y_max = p0[1]
        if p1[1] > y_max: y_max = p1[1]
        if p0[2] > z_max: z_max = p0[2]
        if p1[2] > z_max: z_max = p1[2]
        if p0[2] < z_min: z_min = p0[2]
        if p1[2] < z_min: z_min = p1[2]
        bricks.append([p0, p1])

    x_size = x_max - x_min
    y_size = y_max - y_min
    z_size = z_max - z_min

    # build a cube with -1 values of size x,y,z size, then fill in the bricks
    # starting with the lowest z value, then the next lowest, etc.

    cube = []
    for z in range(z_size+1):
        plane = []
        for y in range(y_size+1):
            row = []
            for x in range(x_size+1):
                row.append(-1)
            plane.append(row)
        cube.append(plane)

    z_max_plane = []
    for y in range(y_size+1):
        row = []
        for x in range(x_size+1):
            row.append(0)
        z_max_plane.append(row)


    # sort bricks by lowest z value
    bricks.sort(key=lambda brick: min(brick[0][2],brick[1][2]))

    # to drop a cube, we just need to know the z_max of the cube for each 
    # x,y, then place at that position and update the z_max to +1 of that level
    # for each of the x,y of the brick. for verticle bricks its +N the height
    # of the brick

    for id, brick in enumerate(bricks):
        p0 = brick[0]
        p1 = brick[1]

        # first determine if we are placing a horizontal or vertical brick
        # if the z values are the same, then we are placing a horizontal brick

        if p0[2] == p1[2]:
            # horizontal brick
            #print(f"horizontal brick")
            if p0[1] == p1[1]:
                # x direction
                y = p0[1]
                #print(f"x direction")

                # first find which plane we hit
                brick_z_max = 0
                for x in range(p0[0], p1[0]+1):
                    brick_z_max = max(brick_z_max, z_max_plane[y][x])

                # now set the z_max for each part of the brick
                for x in range(p0[0], p1[0]+1):
                    z_max_plane[y][x] = brick_z_max + 1

                # now update the brick
                brick[0][2] = z_max_plane[y][x]
                brick[1][2] = z_max_plane[y][x]

                # now place the brick in the cube
                for x in range(p0[0], p1[0]+1):
                    for y in range(p0[1], p1[1]+1):
                        for z in range(p0[2], p1[2]+1):
                            cube[z][y][x] = id

            else:
                # y direction
                x = p0[0]
                #print(f"y direction")

                # first find which plane we hit
                brick_z_max = 0
                for y in range(p0[1], p1[1]+1):
                    brick_z_max = max(brick_z_max, z_max_plane[y][x])

                # now set the z_max for each part of the brick
                for y in range(p0[1], p1[1]+1):
                    z_max_plane[y][x] = brick_z_max + 1

                # now update the brick
                brick[0][2] = z_max_plane[y][x]
                brick[1][2] = z_max_plane[y][x]

                # now place the brick in the cube
                for x in range(p0[0], p1[0]+1):
                    for y in range(p0[1], p1[1]+1):
                        for z in range(p0[2], p1[2]+1):
                            cube[z][y][x] = id

        else:
            # vertical brick
            #print(f"vertical brick")
            x = p0[0]
            y = p0[1]
            height = p1[2] - p0[2] + 1
            oldZMax = z_max_plane[y][x] + 1
            z_max_plane[y][x] = z_max_plane[y][x] + height
            brick[0][2] = oldZMax 
            brick[1][2] = oldZMax + height -1

            # now place the brick in the cube
            for x in range(p0[0], p1[0]+1):
                for y in range(p0[1], p1[1]+1):
                    for z in range(p0[2], p1[2]+1):
                        cube[z][y][x] = id


        #print(brick)
        #printGrid(z_max_plane)

    removedBricks = {}

    for k in range(z_max-1, 0, -1):
        if DEBUG: print(f"\n--[ Layer {k} ]--\n")
        if DEBUG: printGrid(cube[k])

        # get the set of bricks in the relevant planes and if they are connected
        plane_bricks = {}
        lower_plane_bricks = {}
        for x in range(x_size+1):
            for y in range(y_size+1):
                if cube[k-1][y][x] != -1:
                    if cube[k-1][y][x] not in lower_plane_bricks:
                        lower_plane_bricks[cube[k-1][y][x]] = {}
                if cube[k][y][x] != -1:
                    if cube[k][y][x] not in plane_bricks:
                        plane_bricks[cube[k][y][x]] = {}
                if cube[k-1][y][x] != -1 and cube[k][y][x] != -1:
                    lower_plane_bricks[cube[k-1][y][x]][cube[k][y][x]] = True
                    plane_bricks[cube[k][y][x]][cube[k-1][y][x]] = True


        # print the set of bricks we're working with
        if DEBUG: print(f"plane_bricks: {plane_bricks}")
        if DEBUG: print(f"lower_plane_bricks: {lower_plane_bricks}")

        # now we need to figure out which bricks are able to be removed

        known = {}
        states = []

        if puzzlePart == 2:
            initialState = [brick for brick in lower_plane_bricks]
            if DEBUG: print(f"initialState: {initialState}")
            states.append(initialState)
        else:
            for brick in lower_plane_bricks:
                states.append([brick])

        maxRemoveBricks = []

        # TODO: special case top layer?

        while len(states) > 0:
            state = states.pop(0)

            if len(state) == 0:
                if DEBUG: print(f"state is empty")
                continue

            stateString = "_".join([str(i) for i in state])
            if stateString in known:
                if DEBUG: print(f"state is known")
                continue
            known[stateString] = True

            if DEBUG: print(f"state: {state}")

            # see if we can remove all the bricks in the state, if so
            # set to the max and remember the state

            # make a copy of the layer information, then remove each of the
            # bricks in the state. finally pass through the copy and 
            # make sure every brick is still supported. !!! what to do 
            # about verticle or single size bricks?
            test_plane_bricks = {}
            for brick in plane_bricks:
                test_plane_bricks[brick] = {}
                for lower_brick in plane_bricks[brick]:
                   test_plane_bricks[brick][lower_brick] = True

            for brick in state:
                for test_brick in test_plane_bricks:
                    if brick in test_plane_bricks[test_brick]:
                        del test_plane_bricks[test_brick][brick]

            legal = True
            for brick in test_plane_bricks:
                if len(test_plane_bricks[brick]) == 0:
                    # illegal removal
                    if DEBUG: print(f"illegal removal: {brick}")
                    legal = False
                    break

            if legal:
                if puzzlePart == 2:
                    if len(state) > len(maxRemoveBricks):
                        maxRemoveBricks = state.copy()
                        #print(f"--> maxRemoveBricks: {len(maxRemoveBricks)} {maxRemoveBricks} ")
                        continue
                else:
                    removedBricks[state[0]] = True
                    #print(f"--> removedBricks: {state[0]}")
                    continue



            if puzzlePart == 2:
                for brick in state:

                    # otherwise, try to remove one, and then also the rest
                    states.append(state[:1])
                    states.append(state[1:])









    #print(removedBricks)
    return len(removedBricks)

