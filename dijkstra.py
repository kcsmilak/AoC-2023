import tools 

"""
function Dijkstra(Graph, source):
 2      
 3      for each vertex v in Graph.Vertices:
 4          dist[v] ← INFINITY
 5          prev[v] ← UNDEFINED
 6          add v to Q
 7      dist[source] ← 0
 8      
 9      while Q is not empty:
10          u ← vertex in Q with min dist[u]
11          remove u from Q
12          
13          for each neighbor v of u still in Q:
14              alt ← dist[u] + Graph.Edges(u, v)
15              if alt < dist[v]:
16                  dist[v] ← alt
17                  prev[v] ← u
18
19      return dist[], prev[]


1  S ← empty sequence
2  u ← target
3  if prev[u] is defined or u = source:          // Do something only if the vertex is reachable
4      while u is defined:                       // Construct the shortest path with a stack S
5          insert u at the beginning of S        // Push the vertex onto the stack
6          u ← prev[u]                           // Traverse from target to source
"""

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
