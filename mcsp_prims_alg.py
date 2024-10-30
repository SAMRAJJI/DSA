import heapq
def tree(v,e,edges):
    adj=[[]for _ in range(v)]
    pq=[]
    visited =[False]*v
    res=0
    heapq.headpush(pq,(0,0))

    while pq:
        wt, u=headpq.heappop(pq)
        if visited[u]:
            continue
        res +=wt
        visited[u]= True

        for v, weight in adj[u]:
            if not visited[v]:
                headpq.headpop(pq,(weight,v))
        return res

    if __name__=="_main_":
        graph=[[0,1,5],[1,2,3],[0,2,1]]
        print(tree(3,3,graph))

print("--------------------------")

import heapq

def tree(v, e, edges):
    adj = [[] for _ in range(v)]
    for u, vertex, weight in edges:
        if u < v and vertex < v:  # Ensure indices are within range
            adj[u].append((vertex, weight))
            adj[vertex].append((u, weight))
        else:
            raise ValueError(f"Vertex index out of range: {u} or {vertex}")
    pq = []
    visited = [False] * v
    res = 0
    heapq.heappush(pq, (0, 0))  # Start with node 0 and weight 0

    while pq:
        wt, u = heapq.heappop(pq)  # Get the edge with minimum weight
        if visited[u]:
            continue
        res += wt
        visited[u] = True

        # Add all edges from the current node to the priority queue
        for vertex, weight in adj[u]:
            if not visited[vertex]:
                heapq.heappush(pq, (weight, vertex))
    
    return res

if __name__ == "__main__":
    graph = [[0, 1, 5], [1, 2, 3], [0, 2, 1]]
    print(tree(3, 3, graph))


print("--------------------------")
print("gpt code")

import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def print_mst(self, parent):
        print("\nEdge \tWeight")
        mst_weight = 0
        for i in range(1, self.V):
            print(f"{parent[i]} - {i} \t{self.graph[i][parent[i]]}")
            mst_weight += self.graph[i][parent[i]]
        print(f"\nTotal weight of MST: {mst_weight}")

    def min_key(self, key, mst_set):
        min_val = sys.maxsize
        min_index = -1
        for v in range(self.V):
            if key[v] < min_val and not mst_set[v]:
                min_val = key[v]
                min_index = v
        return min_index

    def prim_mst(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mst_set = [False] * self.V
        parent[0] = -1

        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True
            for v in range(self.V):
                if self.graph[u][v] and not mst_set[v] and self.graph[u][v] < key[v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.print_mst(parent)

# Example usage
g = Graph(5)
g.graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

g.prim_mst()

