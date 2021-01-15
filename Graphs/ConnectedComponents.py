#this program contains connected components problem
class Graph:
    def __init__(self):
        self.NoOfNodes=0
        self.graph={}
    def addEdge(self,node1,node2):
        if node1 not in self.graph:
            self.graph[node1]=[]
            self.NoOfNodes+=1
        self.graph[node1].append(node2)
        if node2 not in self.graph:
            self.graph[node2]=[]
            self.NoOfNodes+=1
        self.graph[node2].append(node1)   

    def dfsUtil(self,temp,v,visited):
        visited[v]=True
        temp.append(v)
        for i in self.graph[v]:
            if visited[i]==False:
                self.dfsUtil(temp,i,visited)
        return temp

    def connectedComponents(self):
        visited={v:False for v in self.graph}
        cc=[]
        for v in self.graph:
            if visited[v]==False:
                temp=[]
                cc.append(self.dfsUtil(temp,v,visited))
        return cc 
    


gp=Graph()
gp.addEdge(0,1)
gp.addEdge(1,2)
gp.addEdge(3,4)
print(gp.graph)

li=(gp.connectedComponents())
print(li)


                    


