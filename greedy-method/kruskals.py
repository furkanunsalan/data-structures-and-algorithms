class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    parent[xroot] = yroot

def kruskal_mst(edges, V):
    edges.sort(key=lambda edge: edge.weight)
    parent = [i for i in range(V)]
    total_cost = 0
    edge_count = 0

    for edge in edges:
        x = find(parent, edge.src)
        y = find(parent, edge.dest)

        if x != y:
            total_cost += edge.weight
            union(parent, x, y)
            edge_count += 1
            if edge_count == V - 1:
                break

    return total_cost

if __name__ == "__main__":
    V = 4
    edges = [
        Edge(0, 1, 10),
        Edge(0, 2, 6),
        Edge(0, 3, 5),
        Edge(1, 3, 15),
        Edge(2, 3, 4)
    ]
    print("Total cost of MST:", kruskal_mst(edges, V))
