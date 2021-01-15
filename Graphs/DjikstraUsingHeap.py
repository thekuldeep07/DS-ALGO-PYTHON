# this program will use minHeap to implement Djikstra  and also we will print path information
import heapq

class Graph():
    def __init__(self):
        self.NoOfNodes = 0
        self.graph = {}

    def addEdge(self, node1,node2, wt):
        if node1 not in self.graph:
            self.graph[node1] = {}
            self.NoOfNodes += 1
        if node2 not in self.graph[node1]:
            self.graph[node1][node2] = wt
        if node2 not in self.graph:
            self.graph[node2] = {}
            self.NoOfNodes += 1

    def printPath(self, parent, j, pathQueue):
        if parent[j] == -1:
            pathQueue.append(j)
            return pathQueue
        self.printPath(parent, parent[j], pathQueue)
        pathQueue.append(j)
        return pathQueue

    def djikstra(self, src):
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[src] = 0
        pq = [(0, src)]
        parent = {vertex: -1 for vertex in self.graph}
        while len(pq) > 0:
            currentDistance, currentVertex = heapq.heappop(pq)
            if currentDistance > distances[currentVertex]:
                continue
            for neighbour in self.graph[currentVertex]:
                weight = self.graph[currentVertex][neighbour]
                distance = currentDistance+weight
                if distance < distances[neighbour]:
                    distances[neighbour] = distance
                    parent[neighbour] = currentVertex
                    heapq.heappush(pq, (distance, neighbour))

        for i in self.graph:
            print("source Node (" + str(src)+") -> Distance Node ( " + str(i) +
                  "):\t" + str(distances[i])+"\t Path =",end="")
            path=self.printPath(parent, i, [])
            for i in path:
                print(i,end="->")
            print()    


gp = Graph()
gp.addEdge(0, 1, 5)
gp.addEdge(0, 2, 1)
gp.addEdge(0, 3, 4)
gp.addEdge(1, 0, 5)
gp.addEdge(1, 2, 3)
gp.addEdge(1, 4, 8)
gp.addEdge(2, 0, 1)
gp.addEdge(2, 1, 3)
gp.addEdge(2, 3, 2)
gp.addEdge(2, 4, 1)
gp.addEdge(3, 0, 4)
gp.addEdge(3, 2, 2)
gp.addEdge(3, 4, 2)
gp.addEdge(3, 5, 1)
gp.addEdge(4, 1, 8)
gp.addEdge(4, 2, 1)
gp.addEdge(4, 3, 2)
gp.addEdge(4, 5, 3)
gp.addEdge(5, 3, 1)
gp.addEdge(5, 4, 3)
gp.djikstra(0)
