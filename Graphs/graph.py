class Graph:
    def __init__(self):
        self.noOfNodes=0
        self.graphDict={}

    def addVertex(self,vertex):
        if vertex not in self.graphDict:
            self.graphDict[vertex]=[]
        self.noOfNodes+=1

    def addEdge(self,node1,node2):
        if  node1 in self.graphDict:
            if node2 not in self.graphDict[node1]:
                self.graphDict[node1].append(node2)
        else:
            self.graphDict[node1]=[node2]
    def bfs(sUndirectedelf,node):
        visited=set()
        visited.add(node)
        q=[node]
        while q:
            vertex=q.pop(0)
            print(vertex,end=" ")
            for neighbour in self.graphDict[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    q.append(neighbour)
    def dfs(self,node):
        stack=[node]
        visited=set()
        visited.add(node)
        while stack:
            v=stack.pop()
            print(v,end=" ")
            for i in self.graphDict[v]:
                if i not in visited:
                    stack.append(i)
                    visited.add(i)
    def dfsRecursive(self,node,visited=set()):
        visited.add(node)
        print(node,end=" ")
        for i in self.graphDict[node]:
            if i not in visited:
                self.dfsRecursive(i,visited)               

    def showConnection(self):
        print(self.graphDict)
        

graph=Graph()
graph.addVertex("A")
graph.addVertex("B")
graph.addVertex("C")
graph.addVertex("D")
graph.addVertex("E")
graph.addVertex("F")


graph.addEdge("A","B")
graph.addEdge("A","E")
graph.addEdge("A","C")
graph.addEdge("B","D")
graph.addEdge("C","E")
graph.addEdge("C","F")
graph.showConnection()
graph.bfs("A")
print()
graph.dfs("A")
print()
graph.dfsRecursive("A")


