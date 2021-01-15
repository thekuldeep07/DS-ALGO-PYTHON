class Graph:
    def __init__(self):
        self.noOfNodes=0
        self.graphDict={}
    def addEdge(self,node1,node2):
        if node1 in self.graphDict:
            if node2 not in self.graphDict[node1]:
                self.graphDict[node1].append(node2)
        else:
            self.graphDict[node1]=[node2] 
            self.noOfNodes+=1 

        if node2 not in self.graphDict:
            self.graphDict[node2]=[]
            self.noOfNodes+=1  

    def topologicalSort(self,v,visited=set(),result=[]):
        visited.add(v)
        for vertex in self.graphDict[v]:
            if vertex not in visited:
                self.topologicalSort(vertex,visited,result)
        result.append(v)
        return result[::-1]
graph=Graph()

graph.addEdge(0,1)  
graph.addEdge(0,2)
graph.addEdge(1,2)
graph.addEdge(1,3)
graph.addEdge(2,3)
graph.addEdge(2,4)
print(graph.graphDict)
print(graph.topologicalSort(0))


