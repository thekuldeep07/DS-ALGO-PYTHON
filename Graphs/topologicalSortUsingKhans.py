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

    

    def topoLogicalSort(self):
        indegree=[0]*(len(self.graphDict))
        for i in self.graphDict:
            for j in self.graphDict[i]:
                indegree[j]+=1      
        que=[]
        for i in range(len(indegree)):
            if indegree[i]==0:
                que.append(i)     

        result=[]
        while que:
            u=que.pop(0)
            result.append(u)
            for vertex in self.graphDict[u]:
                indegree[vertex]-=1
                if indegree[vertex]==0:
                    que.append(vertex)
        if len(result)!= self.noOfNodes:
            print("not possible")
        else:
            print(result)        

      



graph=Graph()


graph.addEdge(0,1)  
graph.addEdge(0,2)
graph.addEdge(1,2)
graph.addEdge(1,3)
graph.addEdge(2,3)
graph.addEdge(2,4)
print(graph.graphDict)
graph.topoLogicalSort()

                  

        