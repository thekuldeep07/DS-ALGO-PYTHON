#this program is djikstra algo implementation for finding shortes distance to all Node{ from Source 
#this program uses AdjacencyList representation
import sys
class Graph:
    def __init__(self):
        self.NoOfNodes=0
        self.graphDict={}

    def addEdge(self,node1,node2,wt):
        if node1 not in self.graphDict:
            self.graphDict[node1]={}
            self.NoOfNodes+=1
        if node2 not in self.graphDict[node1]:
            self.graphDict[node1][node2]=wt
        if node2  not in self.graphDict:
            self.graphDict[node2]={}
            self.NoOfNodes+=1   

    def djikstra(self,src):
        distance={i:sys.maxsize for i in self.graphDict} 
        dictlength={src:0}
        distance[src]=0 
        while dictlength:
            sourceNode=min(dictlength,key=lambda k:dictlength[k])
            del dictlength[sourceNode]

            for adjNode in self.graphDict[sourceNode]:
                wt=self.graphDict[sourceNode][adjNode]
                if distance[adjNode] > distance[sourceNode]+wt:
                    distance[adjNode]=distance[sourceNode]+wt
                    dictlength[adjNode]=distance[adjNode]
        for i in self.graphDict:
            print("source Node (" +str(src)+") -> Distance Node ( "+ str(i)+ "):" + str(distance[i]))        


gp=Graph()
gp.addEdge(0,1,5)
gp.addEdge(0,2,1)
gp.addEdge(0,3,4)
gp.addEdge(1,0,5)
gp.addEdge(1,2,3)
gp.addEdge(1,4,8)
gp.addEdge(2,0,1)
gp.addEdge(2,1,3)
gp.addEdge(2,3,2)
gp.addEdge(2,4,1)
gp.addEdge(3,0,4)
gp.addEdge(3,2,2)
gp.addEdge(3,4,2)
gp.addEdge(3,5,1)
gp.addEdge(4,1,8)
gp.addEdge(4,2,1)
gp.addEdge(4,3,2)
gp.addEdge(4,5,3)
gp.addEdge(5,3,1)
gp.addEdge(5,4,3)
gp.djikstra(0)






