#this program will print strongly connected components using Kosraju's algo
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

    def fill_stack(self,d,visited,stack):
        visited[d]=True
        for i in self.graph[d]:
            if not visited[i]:
                self.fill_stack(i,visited,stack)
        stack.append(d)   

    def transpose(self):
        g1=Graph()
        for i in self.graph:
            for j in self.graph[i]:
                g1.addEdge(j,i)
        return g1        

    def dfs(self,d,visited):
        visited[d]=True
        print(d,end=" ")
        for i in self.graph[d]:
            if not visited[i]:
                self.dfs(i,visited)

    def find_scc(self):
        stack=[]
        visited={i:False for i in self.graph}
        for i in self.graph:
            if not visited[i]:
                self.fill_stack(i,visited,stack)
        gr=self.transpose()
        visited={i:False for i in self.graph}
        while stack:
            i=stack.pop() 
            if not visited[i]:
                gr.dfs(i,visited)
                print("")                       
        
g=Graph()
g.addEdge(3,1)
g.addEdge(1,2)
g.addEdge(2,3)

g.addEdge(1,4)
g.addEdge(4,5)
g.find_scc()
