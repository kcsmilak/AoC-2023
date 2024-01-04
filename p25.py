# P1: ? - v225082 ?619225
# P2: ? - ?

# hfx <> pzl
# bvb <> cmg
# nvd <> jqt

#maxEdge = ('khn', 'nrs') c=497156
#maxEdge = ('mqb', 'qlc') c=689515
#maxEdge = ('ssd', 'xqh') c=1238449

import heapq

DEBUG = False

P1E, P1I, P2E, P2I = 54, 619225, None, None



def main():
    #print(f"Ex p1: {run('example.txt')}")
    #print(f"Ex p2: {run('example.txt', 2)}")
    #print(f"In p1: {run('example.txt',2)}")
    print(f"In p2: {run('input.txt',2)}")
    print("__")



def cost(grid, u, v):
    return int(grid[v[1]][v[0]])



def DijkstraP(graph, source, destination = None):
    # Initialize distances and previous vertices
    ds = None
    dist = {}
    prev = {}
    Q = []
    known = {}

    prev[source] = None
    dist[source] = 0

    known[source] = True
    heapq.heappush(Q, (0, source))

    round = 0
    while len(Q) > 0:
        round += 1

        u = heapq.heappop(Q)[1]

        #print(f"u = {u} -> {graph[u]}")

        if not (None == destination):
            pu = (u[0], u[1])
            if pu == destination:
                print(f"Found destination in round {round}")
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


    if not None == destination:
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
    else:
        return dist, prev

def printGraph(graph):
    for node in graph:
        print(f"{node} ->", end="")
        for neighbor in graph[node]:
            print(f" {neighbor}:{graph[node][neighbor]}", end="")
        print()

def removeEdge(graph, a, b):
    # remove that edge and comtinue
    graph[a].pop(b)
    graph[b].pop(a)

def buildGraph(filename):
    graph = {}
    inputLines = open(filename).read().splitlines()
    for i, inputLine in enumerate(inputLines):
        leftComponent = inputLine.split(":")[0]
        if not leftComponent in graph:
            graph[leftComponent] = {}

        rightComponents = inputLine.split(":")[1].strip()
        for rightComponent in rightComponents.split(" "):

            graph[leftComponent][rightComponent] = 1
            if not rightComponent in graph:
                graph[rightComponent] = {}
            graph[rightComponent][leftComponent] = 1
    return graph

def reduceBags2(currentBags):
    bags = []
    for testBag in currentBags:

        componentList = []
        for component in testBag:
            componentList.append(component)


        foundUsableBag = False
        for i, bag in enumerate(bags):
            # if the bag contains any of the components, add all
            for component in componentList:
                if component in bag:
                    foundUsableBag = True
                    break
            if foundUsableBag:
                for component in componentList:
                    bag[component] = True
                break
        if not foundUsableBag:
            bags.append({})
            for component in componentList:
                bags[len(bags)-1][component] = True

    return bags

def reduceMinBags(bags):
    previousLen = -1
    while previousLen != len(bags):
        previousLen = len(bags)
        bags = reduceBags2(bags)
    return bags
def run(filename, puzzlePart=1):

    result = 0

    graph = buildGraph(filename)
    #printGraph(graph)

    if puzzlePart == 1:
        for i in range(3):
            edgeCount = {}
            for start in graph:
                dist,prev = DijkstraP(graph, start, None)

                for destination in graph:
                    if start == destination:
                        continue
                    # get the shortest path to destination
                    S = []
                    u = destination
                    previous = u
                    result = dist[u]
                    if u in prev or u == start:
                        while not u == None:
                            S.insert(0, u)
                            u = prev[u]
                            # add to the edge count
                            a = u
                            b = previous
                            if a == None or b == None:
                                continue
                            if a > b:
                                temp = a
                                a = b
                                b = temp
                            key = (a, b)
                            if not key in edgeCount:
                                edgeCount[key] = 0
                            else:
                                edgeCount[key] += 1
                            previous = u

                    else:
                        raise Exception("Unreachable destination")


            #print(edgeCount)
            maxEdge = None
            maxEdgeCount = 0
            for edge in edgeCount:
                if edgeCount[edge] > maxEdgeCount:
                    maxEdge = edge
                    maxEdgeCount = edgeCount[edge]
            if DEBUG: print(f"maxEdge = {maxEdge} c={maxEdgeCount}")

            removeEdge(graph, maxEdge[0], maxEdge[1])
    else:
        pass
        #removeEdge(graph, "hfx", "pzl")
        #removeEdge(graph, "bvb", "cmg")
        #removeEdge(graph, "nvd", "jqt")

        removeEdge(graph, 'khn', 'nrs') 
        removeEdge(graph, 'mqb', 'qlc') 
        removeEdge(graph, 'ssd', 'xqh') 

    # now reduce the graph and count the bag sizes
    bags = reduceBags(graph)
    bags = reduceBags2(bags)
    if DEBUG: print(len(bags))
    #print(bags)
    bag1size = 0
    bag2size = 0

    for bag in bags[0]:
        bag1size += 1
    for bag in bags[1]:
        bag2size += 1
    result = bag1size * bag2size

    return result


def reduceBags(currentBags):
    bags = []
    for testBag in currentBags:

        componentList = []
        for component in currentBags[testBag]:
            componentList.append(component)


        foundUsableBag = False
        for i, bag in enumerate(bags):
            # if the bag contains any of the components, add all
            for component in componentList:
                if component in bag:
                    foundUsableBag = True
                    break
            if foundUsableBag:
                for component in componentList:
                    bag[component] = True
                break
        if not foundUsableBag:
            bags.append({})
            for component in componentList:
                bags[len(bags)-1][component] = True

    return bags
