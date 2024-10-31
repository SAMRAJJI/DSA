class graph:
    def __init__(self, vertices):
        self.v=vertices
        self.graph=[]

    def addedge(self, u, v, w):
        self.graph.append([u,v,w])

    def find(self, parent, i):
        if parent[i]!=i:
            parent[i]=self.find(parent,parent[i])
        return parent[i]
    def union(self, parent, rank, x, y):
        if rank[x]< rank[y]:
            parent[x]=y
        elif rank[x]> rank[y]:
            parent[y]=x
        else:
            parent[y]=x
            rank[x]+=1

    def kruskalmst(self):
        result=[]
        i=0
        e=0
        self.graph=sorted(self.graph, key=lambda item: item[2])
        parent=[]
        rank=[]
        for node in range(self.v):
            parent.append(node)
            rank.append(0)

        while e< self.v-1:
            u,v,w=self.graph[i]
            i=i+1
            x=self.find(parent, u)
            y=self.find(parent, v)

            if x!=y:
                e=e+1
                result.append([u,v,w])
                self.union(parent, rank, x, y)
    
        minimumcost=0
        print("edges in the constructed MST")
        for u, v, weight in result:
            minimumcost+= weight
            print("%d--%d==%d"%(u, v, weight))
        print("minimum spanning tree", minimumcost)

if __name__=="__main__":
    g=graph(4)
    g.addedge(0,1,10)
    g.addedge(0,2,6)
    g.addedge(0,3,5)
    g.addedge(1,3,15)
    g.addedge(2,3,4)
    g.kruskalmst()




print("\n#gpt code\n")


class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    def kruskal_mst(self):
        result = []  # Store the resulting MST
        i = 0        # Initial index for sorted edges
        e = 0        # Count of edges in MST

        # Sort all edges based on weight
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        # Initialize parent and rank
        for node in range(self.v):
            parent.append(node)
            rank.append(0)

        # Process edges in sorted order
        while e < self.v - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge does not cause a cycle
            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        minimum_cost = 0
        print("Edges in the constructed MST:")
        for u, v, weight in result:
            minimum_cost += weight
            print(f"{u} -- {v} == {weight}")
        print("Minimum Spanning Tree Cost:", minimum_cost)


# Driver code
if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)

    g.kruskal_mst()

