import sys

def min_distance(dist, spt_set):
    min_value = sys.maxsize
    min_index = -1
    for v in range(len(dist)):
        if not spt_set[v] and dist[v] < min_value:
            min_value = dist[v]
            min_index = v
    return min_index

def dijkstra(graph, src):
    V = len(graph)
    dist = [sys.maxsize] * V
    dist[src] = 0
    spt_set = [False] * V

    for _ in range(V):
        u = min_distance(dist, spt_set)
        spt_set[u] = True

        for v in range(V):
            if graph[u][v] and not spt_set[v] and dist[u] != sys.maxsize and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]

    return dist

if __name__ == "__main__":
    graph = [
        [0, 10, 0, 0, 0, 0],
        [10, 0, 5, 0, 0, 0],
        [0, 5, 0, 20, 1, 0],
        [0, 0, 20, 0, 2, 0],
        [0, 0, 1, 2, 0, 3],
        [0, 0, 0, 0, 3, 0]
    ]
    dist = dijkstra(graph, 0)
    print("Shortest distances from source:", dist)
