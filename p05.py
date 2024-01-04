# P1: ? - ?
# P2: 1561682361 - ?

P1E, P1I, P2E, P2I = 35, 227653707, 46, None

DEBUG = False
DEBUG2 = False
DEBUG3 = False
DEBUG4 = False
CRAZY = False
EXAMPLE, INPUT =  True, False
PART1, PART2 = True, False

# 1561682361
# 3510499789 > 1170160938 > 1166153959 > 599659483
# 599,659,483 is too high!! as is 541068756
# 6,210,005,621

# 1,017,608,497 is too high! range (1000000000- 1050000000)) [15 mins]
def getSeedLocation(maps, seed):
    if DEBUG or DEBUG3: print(f"Seed: {seed}", end="")
    for map in maps:
        if DEBUG: print(f"Map:")
        for row in map:
            if DEBUG: print(f"  Row: {row}")
    
            destinationStart = row[0]
            sourceStart = row[1]
            range = row[2]
    
            diff = seed - sourceStart
            if seed >= sourceStart and seed < sourceStart + range:
                newseed = destinationStart + diff
                #if DEBUG: print(f"    -> Moved: {seed} to {newseed}")
                #if DEBUG3: print(f" > {newseed:2}", end="")
                seed = newseed
                break
    if DEBUG or DEBUG3: print("\t",seed)
    return seed

def getLocationSeed(maps, source):
    if DEBUG or DEBUG3: print(f"Location: {source}", end="")

    for i in range(len(maps)):
        mapi = len(maps) - i -1 
        map = maps[mapi]
        if DEBUG4: print(f"Map: {mapi} = {map}")
        #map.reverse()
        for row in map:
            if DEBUG3: print(f"  Row: {row}")
            sourceStart = row[0]
            destinationStart = row[1]
            plantRange = row[2]
            diff = source - sourceStart
            if source >= sourceStart and source < sourceStart + plantRange:
                destination = destinationStart + diff
                if DEBUG3: print(f"    -> Moved: {source} to {destination}")
                if DEBUG3: print(f" > {destination:2}", end="")
                source = destination
                break
    if DEBUG or DEBUG3: print()
    return source


def sortMap(map1):
    map1.sort(key=lambda x: x[1])

def fillRange(map1, max):
    if map1[0][1] != 0:
        map1.insert(0, [0, 0, map1[0][1]])
    if map1[len(map1)-1][1] + map1[len(map1)-1][2] < max:
        start = map1[len(map1)-1][1] + map1[len(map1)-1][2]        
        map1.append([start, start, max-start])
        
def mergeMaps(leftMap, rightMap):
    sortMap(leftMap)
    fillRange(leftMap, 100)
    #print(leftMap)
    
    sortMap(rightMap)
    fillRange(rightMap, 100)
    #print(rightMap)

    mergedMap = []

    leftMapIndex = 0
    rightMapIndex = 0

    i = 0
    offset = 0
    while True:

        leftRange = leftMap[leftMapIndex]
        rightRange = rightMap[rightMapIndex]

        #print(f"working on {leftRange} and {rightRange}")

        leftModifier = leftRange[1] - leftRange[0]
        rightModifier = rightRange[1] - rightRange[0]

        leftStart = leftRange[1]
        leftLength = leftRange[2]
        leftEnd = leftRange[1] + leftRange[2] - 1
        rightStart = rightRange[1]
        rightLength = rightRange[2]
        rightEnd = rightRange[1] + rightRange[2] - 1

        if leftEnd == rightEnd:
            #print("perfect match")
            leftMapIndex += 1
            rightMapIndex += 1
        elif leftEnd < rightEnd:
            #print(f"working left")
            leftMapIndex += 1
            pass
        else:
            #print(f"splitting left with right at {rightEnd}")

            rightMapIndex += 1
            
            pass
            
            pass

        # 4 possibilities:
        # 1. left finishes before right
        
        
        
        i += 1
        if i > 100 : break


def run(filename, modifier=False):

    maps = []
    curMap = []
    lines = open(filename).read().splitlines()

    seed_list = [int(x) for x in lines[0].split(": ")[1].split(" ")]
            
    for i, line in enumerate(lines[2:]):

        if line.endswith("map:"):
            curMap.clear()
            continue
        
        if len(line) == 0:
            maps.append(curMap.copy())
            continue

        curMap.append([int(x) for x in line.split(" ")])

        if i+2 == len(lines)-1:
            maps.append(curMap.copy())
            continue

    mergeMaps(maps[0], maps[1])
    return

    #print(getSeedLocation(maps, test))
    #print(getLocationSeed(maps, test))

    #if DEBUG: print(f"Maps: {maps}")

    if not modifier:
        lowestLocation = None
        for seed in seed_list:
    
            if DEBUG or DEBUG2: print(f"Seed: {seed}")

            location = getSeedLocation(maps, seed)
            if DEBUG2: print(f"  checking seed {seed} -> {location}")
    
    
            if lowestLocation is None or location < lowestLocation:
                lowestLocation = location
                print("    -> Lowest location:", lowestLocation)
                
        return lowestLocation
    else:

        
        #if DEBUG: print(f"Maps: {maps}")
        lowestLocation = None

        #lets check some ranges
        seed = seed_list[0]
        location = getLocationSeed(maps, seed)
        print(f"{location:,}")


        lowestLocation = 599659483
        location = lowestLocation
        while(True):
            if location < 0: 
                print("ZERO LOCATION")
                break
            location = location - 1
            if location % 100000 == 0:
                print(".", end="", flush=True)
            
           
            seed = getLocationSeed(maps, location)

            # see if the seed is in range
            inRange = False
            for i in range(len(seed_list) // 2):
                rangeStart = seed_list[i*2]
                rangeLength = seed_list[i*2+1]
                rangeEnd = rangeStart + rangeLength
                # if seed in range
                if seed >= rangeStart and seed < rangeEnd:
                    print(f"WINNER!!!! {seed} -> {location}")
                    inRange = True
                    break
            if not inRange:
                continue


            
            seedLocation = getSeedLocation(maps, seed)
            if seedLocation < lowestLocation:
                lowestLocation = seedLocation
                print(f"  {location:,} -> {seedLocation:,}")
                
        
        
        
        print()

        if False:

            start =         1050000000
            scope = start + 500000000
            start = 0 
            scope = 100
            print(f"testing if location will be in scope: {start} -> {scope}")
            for location in range(start, scope):
                seed = getLocationSeed(maps, location)
                if DEBUG4: print(f"Location {location} -> {seed}")
    
                # see if seed in a current plant range
                for i in range(len(seed_list) // 2):
                    rangeStart = seed_list[i*2]
                    rangeLength = seed_list[i*2+1]
                    rangeEnd = rangeStart + rangeLength
                    # if seed in range
                    if seed >= rangeStart and seed < rangeEnd:
                        print(f"WINNER!!!! {seed} -> {location}")
                        return location
    
                div = 100000
                if location % div == 0: print(f".{location//div}", end="", flush=True)
        
        return -1 


