def floydwarshall(graph):
    distance = {}
    predesessor = {}
    for u in graph:
        distance[u] = {}
        predesessor[u] = {}
        for v in graph:
            distance[u][v] = 1000
            predesessor[u][v] = -1
        distance[u][u] = 0
        for neighbor in graph[u]:
            distance[u][neighbor] = graph[u][neighbor]
            predesessor[u][neighbor] = u

    for t in graph:
        for u in graph:
            for v in graph:
                newdistance = distance[u][t] + distance[t][v]
                if newdistance < distance[u][v]:
                    distance[u][v] = newdistance
                    # make a new route through t
                    predesessor[u][v] = predesessor[t][v]

    return distance, predesessor


graph = {0: {1: 6, 2: 8},
         1: {4: 11},
         2: {3: 9},
         3: {},
         4: {5: 3},
         5: {2: 7, 3: 4}}

distance, predesessor = floydwarshall(graph)
for v in predesessor:
    print("%s: %s" % (v, predesessor[v]))
for v in distance:
    print("%s: %s" % (v, distance[v]))
