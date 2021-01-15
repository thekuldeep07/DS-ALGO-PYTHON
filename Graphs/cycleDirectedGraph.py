class Graph:
    def __init__(self):
        self.NoofNodes=0
        self.graph={}

    def addEdge(self,node1,node2):
        if node1 not in self.graph:
            self.graph[node1]=[]
            self.NoofNodes+=1
        
        self.graph[node1].append(node2)
        if node2 not in self.graph:
            self.graph[node2]=[]
            self.NoofNodes+=1

    def isCyclicUtil(self,node,visited,recStack):
        visited[node]=True
        recStack[node]=True
        for neighbour in self.graph[node]:
            if not visited[neighbour]:
                if self.isCyclicUtil(neighbour,visited,recStack):
                    return True
            elif recStack[neighbour]:
                return True
        recStack[node]=False
        return False                

    


    def findCycle(self):
        visited={vertex:False for vertex in self.graph}
        recStack={vertex:False for vertex in self.graph}
        for node in self.graph:
            if visited[node]==False:
                if self.isCyclicUtil(node,visited,recStack):
                    return True
        return False            

gp=Graph()                    
gp.addEdge(0,1)
gp.addEdge(0,2)
gp.addEdge(1,2)
gp.addEdge(2,3)
print(gp.graph)
val=gp.findCycle()
print(val)
