import sys
class Graph():
    def __init__(self):
        self.noOfNodes=0
        self.graph = {}

    def addEdge(self,node1,node2,wt):
        if node1 not in self.graph:
            self.graph[node1]={}
            self.noOfNodes+=1
        self.graph[node1][node2]=wt
        if node2 not in self.graph :
            self.graph[node2]={}
            self.noOfNodes+=1
    def printPath(self, parent, j, pathQueue):
        if parent[j] == -1:
            pathQueue.append(j)
            return pathQueue
        self.printPath(parent, parent[j], pathQueue)
        pathQueue.append(j)
        return pathQueue

    def bellmanFord(self,src):
        dist={vertex:sys.maxsize for vertex in self.graph}
        dist[src]=0 
        parent={vertex:-1 for vertex in self.graph}
        updated=False
        for node in self.graph:
            for neighbour in self.graph[node]:
                cost=self.graph[node][neighbour]
                if (dist[node]+ cost) < dist[neighbour]:
                    dist[neighbour]= dist[node]+cost
                    parent[neighbour]=node
        for node in self.graph:
            for neighbour in self.graph[node]:
                cost=self.graph[node][neighbour]
                if (dist[node]+ cost) < dist[neighbour]:
                    print("nn")           
        
        for i in self.graph:
            print("source Node (" + str(src)+") -> Distance Node ( " + str(i) +
                  "):\t" + str(dist[i])+"\t Path =",end="")
            path=self.printPath(parent, i, [])
            for i in path:
                print(i,end="->")
            print() 
       
                      
g=Graph()
g.addEdge(0,1,-1)
g.addEdge(0,2,4)
g.addEdge(1,2,3)
g.addEdge(1,3,2)
g.addEdge(1,4,2)
g.addEdge(3,2,5)
g.addEdge(3,1,1)
g.addEdge(4,3,-3)
g.bellmanFord(0)