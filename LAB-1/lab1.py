import heapq

def aStarAlgo(start_node, stop_node):
    open_set = [(0, start_node)]
    closed_set = set()
    g = {start_node: 0}
    parents = {start_node: start_node}
    while open_set:
        f, n = heapq.heappop(open_set)
        if n == stop_node:
            return check(parents, n, start_node)
        closed_set.add(n)
        for m, weight in get_neighbors(n):
            if m in closed_set:
                continue
            if m not in g or g[m] > g[n] + weight:
                g[m] = g[n] + weight
                parents[m] = n
                heapq.heappush(open_set, (g[m] + heuristic(m), m))
    return None

def check(parents, n, start_node):
    path = []
    while n != start_node:
        path.append(n)
        n = parents[n]
    path.append(start_node)
    print(f'Path found: {path[::-1]}')
    return path[::-1]

def get_neighbors(v):
    return Graph_nodes[v] if v in Graph_nodes else None

def heuristic(n):
    H_dist = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0,
        }
    return H_dist[n]

Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': None,
    'E': [('D', 6)],
    'D': [('G', 1)],
    }

aStarAlgo('A', 'G')