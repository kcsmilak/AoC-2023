import tools 

def cost(grid, u, v):
    return int(grid[v[1]][v[0]])
    
def Dijkstra(grid, source, destination):
    # Initialize distances and previous vertices
    dist = {}
    prev = {}
    Q = {}
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            v = (x,y)
            dist[v] = float('inf')
            prev[v] = None
            Q[v] = True

    dist[source] = 0
    
    while len(Q) > 0:
        
        # lazy method, sort the keys and get min
        u = None
        minDist = float('inf')
        for v in Q:
            if dist[v] < minDist:
                minDist = dist[v]
                u = v
                
        if u == destination:
            break

        del Q[u]
        
        # get adjacent values of u
        for offset in tools.OFFSETS:
            v = u[0]+offset[0], u[1]+offset[1]
            if v[0]<0 or v[0]>=len(grid[0]) or v[1]<0 or v[1]>=len(grid):
                continue # out of range
            if not v in Q:
                continue
            alt = dist[u] + cost(grid, u, v)
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                
    S = []
    u = destination
    result = 0 
    if u in prev or u == source:
        while not u == None:
            if u != source:
                result += cost(map,u,u)
            S.insert(0, u)
            u = prev[u]
    else:
        raise Exception("Unreachable destination")
    
    return S, result
    #return dist, prev
                


filename = "dijkstra.in"
inputLines = open(filename).read().splitlines()
map = []
start = None
for i, inputLine in enumerate(inputLines):
    map.append([x for x in inputLine])

#map = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
source = (0,0)
destination = (2,2)
tools.printMap(map)
print()
print(Dijkstra(map, (source), destination))
