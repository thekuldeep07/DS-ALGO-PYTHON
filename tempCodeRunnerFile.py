 def addVertex(self,vertex):
        if vertex not in self.graphDict:
            self.graphDict[vertex]=[]
        self.noOfNodes+=1