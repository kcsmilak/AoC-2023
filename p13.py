# P1: 405 - 37718
# P2: x29366 (low) - 36810 too low -- 27901 too low -- 28840? --> 40995

DEBUG1 = False

def main():
    print(f"1t: {run('13.tst')}")
    print(f"1e: {run('13.ex')}")
    #print(f"1i: {run('13.in')}")
    print(f"2t: {run('13.tst', 2)}")
    #print(f"2e: {run('13.ex', 2)}")
    print(f"2i: {run('13.in', 2)}")
    print("________________________________________________")

def mapString(map):
    return "\n".join("".join(map[y][x] for x in range(len(map[0]))) for y in range(len(map)))
    
def findMatchs(hashList, map = None, firstResult = -1):
    
    matches = []
    #matchi = 0
    for i in range(0, len(hashList)):
        

        left = hashList[:i+1]
        left.reverse()
        right = hashList[i+1:]
        
        data = [] 
        if not map == None:
            data = map[i] 
        
        #print(f"comparing d[{data}]\n\t{left}\n\t{right}")

        if len(left) <= 0 or len(right) <= 0:
            break
        match = True
        offset = 0
        while True:
            if offset >= len(left):
                break 
            if offset >= len(right):
                break
            if left[offset] != right[offset]:
                match = False
                break
            offset += 1
        if match:
            print(f"--> Match at {i+1} with size {offset} and first {firstResult}")
            matches.append(i+1)
            #matchi= i+1
            #if (-1 == firstResult): return matchi
            continue
    return matches
  


def mapMirror(map, firstResult = -1):
    results = []
    
    invertedMap = []

    for j, col in enumerate(map[0]):
        data = []
        for i, row in enumerate(map):
            data.append(map[i][j]) 
        invertedMap.append(data)

    if DEBUG1: print()
    if DEBUG1: print(mapString(map))

    hashList = []
    for i, row in enumerate(map):
        data = "".join(row)
        hashList.append(hash(data))

    
    match1 = findMatchs(hashList, map, firstResult)
    for match in match1:
        results.append(100*match)
    if len(match1) > 0:
        if DEBUG1: print(f"Match1: {match1}\n")

    hashList = []
        
    if DEBUG1: print(mapString(invertedMap)) 

    for i, row in enumerate(invertedMap):
        data = "".join(row)
        hashList.append(hash(data))
        
    match2 = findMatchs(hashList,invertedMap, firstResult) 
    for match in match2:
        results.append(match)
    if len(match2) > 0:
        if DEBUG1: print(f"Match2: {match2}\n")


    return results

    if (match1 > 0 and match2 > 0): 
        #print(f"DOUBLE MATCH: {match1} {match2}")
        if match1 * 100 == firstResult:
            return match2
        elif match2 == firstResult:
            return match1 * 100
        raise Exception()
    if (match1 == 0 and match2 == 0):
        #print("NO MATCH")
        return -1
        
    result += match1 * 100 + match2
    
    return result

def deepCopy(map):
    mapCopy = []
    for y, row in enumerate(map):
        rowCopy = []
        for x, col in enumerate(row):
            rowCopy.append(row[x])
        mapCopy.append(rowCopy)
    return mapCopy

def run(filename, puzzlePart = 1):


    result = 0

    maps = []
    buffer = []
     
    inputLines = open(filename).read().splitlines()
    
    i = 0
    while i <= len(inputLines):
        if i >= len(inputLines) or len(inputLines[i]) == 0 :
            maps.append(buffer)
            buffer = []
        else:
            buffer.append([x for x in inputLines[i]])
        i+=1
    
    for im in range(len(maps)):
        
        map = maps[im]
        
        if puzzlePart == 1:
            result += mapMirror(map)[0]
        else:
            firstResult = mapMirror(map)[0]

            #print()
            #print(mapString(map))
            print(f"first match {firstResult}")
    
            done = False
            for y, row in enumerate(map):
                if done: break
                for x, col in enumerate(row):
                    if done: break
                
                    if (x,y) == (11,8):
                        print(mapString(map))
                
                    if map[y][x] == '.':
                        map[y][x] = '#'
                        if (x,y) == (11,7):
                            #print("---------------------------------")
                            #print(mapString(map))
                            pass
                        secondResult = mapMirror(map, firstResult)
                        #print(secondResult)
                        if len(secondResult) != 0:
                            
                            print(f"found #: {secondResult} using {x},{y}")
                            #print(mapString(map))
                            
                            for r in secondResult:
                                
                                if r != firstResult: 
                                    result += r
                                    print(f"addding {r}")
                            #result += secondResult[0]
                                    done = True
                        map[y][x] = '.'
                    else:
                        map[y][x] = '.'
                        secondResult = mapMirror(map, firstResult)
                        #print(secondResult)
                        if secondResult != -1 :
                            print(f"found .: {secondResult} using {x},{y}")
                            #print(mapString(map))
                            for r in secondResult:
                                if r != firstResult: 
                                    result += r
                                    print(f"addding {r}")
                                    done = True
                        map[y][x] = '#'
            #if not done:
            #    print(mapString(map))
            #    raise Exception("ugh")
                        
            
    return result

main()
