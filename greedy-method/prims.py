import sys

def prim_mst(graph):
    V = len(graph)
    key = [sys.maxsize] * V
    key[0] = 0
    mst_set = [False] * V
    parent = [-1] * V

    for _ in range(V):
        u = min_key(key, mst_set)
        mst_set[u] = True

        for v in range(V):
            if graph[u][v] and not mst_set[v] and graph[u][v] < key[v]:
                parent[v] = u
                key[v] = graph[u][v]

    total_cost = sum(graph[i][parent[i]] for i in range(1, V))
    return total_cost

def min_key(key, mst_set):
    min_value = sys.maxsize
    min_index = -1
    for v in range(len(key)):
        if not mst_set[v] and key[v] < min_value:
            min_value = key[v]
            min_index = v
    return min_index

if __name__ == "__main__":
    graph = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0]
    ]
    print("Total cost of MST:", prim_mst(graph))
