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
              

    def BFSCycle(self,src):
        visited=set()
        q=[(src,-1)]
        visited.add(src)
        while q:
            (v,parent)=q.pop(0)
            for vertex in self.graphDict[v]:
                if vertex not in visited:
                    visited.add(vertex)
                    q.append((vertex,v))
                elif vertex !=parent:
                    return True
        return False  

    def dfsCyclDetection(self,src,visited=set(),parent=None):
        visited.add(src)
        for vertex in self.graphDict[src]:
            if vertex not in visited :
                if self.dfsCyclDetection(vertex,visited,src):
                    return True
            elif vertex!=parent:
                print(vertex,parent,src)
                return True
        return False

    def showConnection(self):
        print(self.graphDict)        


graph=Graph()

graph.addEdge(1,2)
graph.addEdge(2,3)
graph.addEdge(3,4)
graph.addEdge(4,5)
graph.addEdge(5,6)
graph.addEdge(6,1)
graph.addVertex(7)

graph.showConnection()
print(graph.BFSCycle(1))
print(graph.dfsCyclDetection(1))
