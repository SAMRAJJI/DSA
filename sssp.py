import sys
class graph():
    def __init__(self, vertice):
        self.v = vertice
        self.graph =[[0 for column in range(vertice)]for row in range(vertice)]
    def printsol(self, dist):
        print( "vertex \t distance from source")
        for node in range(self.v):
            print (node,"\t", dist[node])
    def mindistance(self, dist, sptset):
        ## min=sys.maxint
         min_val = float('inf')
         min_index = -1
         for u in range(self.v):
            if dist[u] < min_val and sptset[u]== False:
                min_val = dist[u]
                min_index = u
         return min_index
        
    def dijkstra(self,src):
        dist=[float('inf')]*self.v
        dist[src]=0
        sptset=[False]*self.v
        for count in range(self.v):
            x=self.mindistance(dist, sptset)
            sptset[x] = True
            for y in range(self.v):
                if self.graph[x][y]>0 and not sptset[y] and dist[y]> dist[x]+ self.graph[x][y]:
                    dist[y]=dist[x]+self.graph[x][y]
        self.printsol(dist)

g=graph(9)

g.graph=[[0,4,0,0,0,0,0,8,0],
         [4,0,8,0,0,0,0,11,0],
         [0,8,0,7,0,4,0,0,2],
         [0,0,7,0,9,14,0,0,0],
         [0,0,0,9,0,10,0,8,0],
         [0,0,4,14,10,0,2,0,0],
         [0,0,0,0,0,2,0,1,6],
         [8,11,0,0,0,0,1,0,7],
         [0,0,2,0,0,0,6,7,0]
         ]
g.dijkstra(0)





##import sys
##
##class Graph():
##    def __init__(self, vertice):
##        self.v = vertice
##        self.graph = [[0 for column in range(vertice)] for row in range(vertice)]
##
##    def printsol(self, dist):
##        print("Vertex \t Distance from Source")
##        for node in range(self.v):
##            print(node, "\t", dist[node])
##
##    def mindistance(self, dist, sptset):
##        min_val = float('inf')
##        min_index = -1
##
##        for u in range(self.v):
##            if dist[u] < min_val and sptset[u] == False:
##                min_val = dist[u]
##                min_index = u
##        return min_index
##
##    def dijkstra(self, src):
##        dist = [float('inf')] * self.v
##        dist[src] = 0
##        sptset = [False] * self.v
##
##        for count in range(self.v):
##            x = self.mindistance(dist, sptset)
##            sptset[x] = True
##
##            for y in range(self.v):
##                if self.graph[x][y] > 0 and sptset[y] == False and dist[y] > dist[x] + self.graph[x][y]:
##                    dist[y] = dist[x] + self.graph[x][y]
##
##        self.printsol(dist)
##
### Driver code
##g = Graph(9)
##g.graph = [
##    [0, 4, 0, 0, 0, 0, 0, 8, 0],
##    [4, 0, 8, 0, 0, 0, 0, 11, 0],
##    [0, 8, 0, 7, 0, 4, 0, 0, 2],
##    [0, 0, 7, 0, 9, 14, 0, 0, 0],
##    [0, 0, 0, 9, 0, 10, 0, 8, 0],
##    [0, 0, 4, 14, 10, 0, 2, 0, 0],
##    [0, 0, 0, 0, 0, 2, 0, 1, 6],
##    [8, 11, 0, 0, 0, 0, 1, 0, 7],
##    [0, 0, 2, 0, 0, 0, 6, 7, 0]
##]
##g.dijkstra(0)
