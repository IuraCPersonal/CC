def dijkstra(graph_dict, start, end):
    if not start in graph_dict:
        raise ValueError('missing {0}'.format(start))
    if not end in graph_dict:
        raise ValueError('missing {0}'.format(end))

    nodes = graph_dict.keys()

    f = float('inf')
    dist_from_start = {n: f for n in nodes}
    dist_from_start[start] = 0
    predecessors = {n: None for n in nodes}

    while len(nodes) > 0:
        candidates = {n: dist_from_start[n] for n in nodes}
        closest = min(candidates, key=candidates.get)  # ref footnote 2

        for n in graph_dict[closest]:
            if not n in dist_from_start:
                msg = 'missing node {0} (neighbor of {1})'.format(n, closest)
                raise ValueError(msg)
            dist_to_n = graph_dict[closest][n]
            if dist_to_n < 0:
                msg = 'negative distance from {0} to {1}'.format(closest, n)
                raise ValueError(msg)
            d = dist_from_start[closest] + dist_to_n
            if dist_from_start[n] > d:
                dist_from_start[n] = d
                predecessors[n] = closest

        nodes.remove(closest)

    return (dist_from_start, predecessors)


def shortestPath(graph_dict, start, end):
    distances, predecessors = dijkstra(graph_dict, start, end)

    if predecessors[end] is None and start != end:
        return [], distances[end]

    path = [end]
    while path[-1] != start:
        path.append(predecessors[path[-1]])
    path.reverse()

    return path, distances[end]


if __name__ == '__main__':
    from test import test_fixtures
    G = test_fixtures.test_fixtures['multinode']
    print(G)
    path, total_distance = shortestPath(G, 'a', 'e')
    msg = 'Shortest distance from a to e is {0}, total distance {1}.'
    print(msg.format(' -> '.join(path), total_distance))
