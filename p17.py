import tools
import heapq

# 1213 is too low, 1223 is too high --> 1215 (50s)

def gridCost(grid, u, v):
    return int(grid[v[1]][v[0]])


def DijkstraP(graph, source, destination):
    # Initialize distances and previous vertices
    ds = None
    dist = {}
    prev = {}
    Q = []
    known = {}

    prev[source] = None
    dist[source] = 0

    #for v in graph:
    #    dist[v] = float('inf')
    #    prev[v] = None
    #    #Q[v] = True
    #    heapq.heappush(Q, (dist[v], v))
    known[source] = True
    heapq.heappush(Q, (0, source))

    round = 0
    while len(Q) > 0:
        round += 1

        u = heapq.heappop(Q)[1]
        #print(f"u = {u} -> {graph[u]}")

        pu = (u[0], u[1])
        if pu == destination and u[3]>3:
            print(f"Found destination in round {round} step {u[3]}")
            ds = u
            break
            #pass

        if u is None:
            print(Q)
            raise Exception("invalid u = None = ", round)

        # get adjacent values of u
        for v in graph[u]:
            #print(f" v = {v}")
            if not v in dist:
                dist[v] = float('inf')
            if not v in prev:
                prev[v] = None

            alt = dist[u] + graph[u][v]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                if not v in known:
                    known[v] = True
                    heapq.heappush(Q, (dist[v], v))

    #print(f"d{dist}")
    #print(f"p{prev}")


    S = []
    u = ds
    result = dist[u]
    if u in prev or u == source:
        while not u == None:
            S.insert(0, u)
            u = prev[u]
    else:
        raise Exception("Unreachable destination")

    return S, result
    #return dist, prev


def run(filename, puzzlePart=1):

    inputLines = open(filename).read().splitlines()
    map = []
    start = None
    for i, inputLine in enumerate(inputLines):
        map.append([x for x in inputLine])
    
    source = (0,0)
    destination = (len(map[0])-1,len(map)-1)
    #tools.printMap(map)
    #print()
    #print(Dijkstra(map, (source), destination))
    
    states = {}
    if puzzlePart == 1:
        for y in range(len(map)):
            for x in range(len(map[0])):
                for d in range(len(tools.DIRECTIONS)):
                    for s in range(0,3):
                        key = (x,y,d,s)
                        states[key] = {}
    
                        # create the output states
                        for nd in range(len(tools.DIRECTIONS)):
    
                            # check if location is on the map
                            offset = tools.OFFSETS[nd]
                            v = x+offset[0], y+offset[1]
                            if v[0]<0 or v[0]>=len(map[0]) or v[1]<0 or v[1]>=len(map):
                                continue # out of range
    
                            if nd == d:
                                # add a step and move forward
                                ns = s+1
                                if ns == 3:
                                    continue
                                pass
                            elif nd == (d+2)%4:
                                # skip, cannot go backwards
                                continue    
                            else:
                                # reset steps, then attempt to move
                                ns = 0
                                pass
    
                            nkey = (v[0],v[1],nd,ns)
                            ncost = gridCost(map, (x,y), v)
                            states[key][nkey] = ncost
    else:
        for y in range(len(map)):
            for x in range(len(map[0])):
                for d in range(len(tools.DIRECTIONS)):
                    for s in range(0,10):
                        key = (x,y,d,s)
                        states[key] = {}
                        finished = False
                        # create the output states
                        for nd in range(len(tools.DIRECTIONS)):
    
                            # check if location is on the map
                            offset = tools.OFFSETS[nd]
                            v = x+offset[0], y+offset[1]
                            if v[0]<0 or v[0]>=len(map[0]) or v[1]<0 or v[1]>=len(map):
                                continue # out of range
    
                            if nd == d:
                                # add a step and move forward
                                ns = s+1
    
                                if ns == 10:
                                    continue
                                pass
                            elif nd == (d+2)%4:
                                # skip, cannot go backwards
                                continue    
                            elif s >= 3:
                                # reset steps, then attempt to move
                                ns = 0
                                pass
                            else:
                                continue
    
                            nkey = (v[0],v[1],nd,ns)
                            ncost = gridCost(map, (x,y), v)
                            states[key][nkey] = ncost
    
    
    #print(states)
    print(f"make {len(states)} states")
    
    
    source = (0,0,1,0)
    path, cost = DijkstraP(states, source, destination)
    print(f"Cost: {cost}   PathLength: {len(path)}")
    
    source = (0,0,2,0)
    path, cost = DijkstraP(states, source, destination)
    print(f"Cost: {cost}   PathLength: {len(path)}")


#print(path)


