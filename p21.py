# P1: ? - ?
# P2: ? - ?

DEBUG = True

def main():
    #print(f"Ex p1: {run('test.txt')}")
    print(f"Ex p1: {run('example2.txt')}")
    #print(f"Ex p2: {run('example.txt', 2)}")
    #print(f"In p1: {run('input.txt')}")
    #print(f"In p2: {run('input.txt', 2)}")
    print("__")

def printMap(map, start = None, plots = None):
    print()
    count = 0
    for y, row in enumerate(map):
        for x, c in enumerate(row):
            if not start == None and start == (x,y):
                c = "S"
            if not plots == None and (x,y) in plots:
                c = "O"
            
            print(c, end='')
            if c == 'O': 
                count+=1
        print()
    print(f"count = {count}")

def run(filename, puzzlePart = 1):

    result = 0

    inputLines = open(filename).read().splitlines()
    map = []
    start = None
    for i, inputLine in enumerate(inputLines):
        map.append([x for x in inputLine])
        if inputLine.find('S') != -1:
            start = (inputLine.find('S'),i)
            
    map[start[1]][start[0]] = '.'
    #printMap(map)
    #print(start)

    plots = {}
    plots[start] = True
    
    maxRounds = 12
    while True:
        if maxRounds <= 0:
            break
        maxRounds -= 1

        newPlots = {}
        for plot in plots:
            x,y = plot
            for offset in [(0,1),(0,-1),(1,0),(-1,0)]:
                newX = x + offset[0]
                newY = y + offset[1]


                if newX < 0 or newX >= len(map[0]) or newY < 0 or newY >= len(map):
                    continue
                if map[newY][newX] == '.':
                    #print(f"plot {plot} -> {newX},{newY}")
                    newPlots[(newX,newY)] = True


        printMap(map, start, plots)
        plotList = list(plots.keys())
        plotList.sort()
        #print(f"plotList = {plotList}")
        plotHashString = ''.join([f"{x},{y}" for x,y in plotList])
        
            
        print(hash(plotHashString))

        plots = newPlots                    
    
    return len(plots)

