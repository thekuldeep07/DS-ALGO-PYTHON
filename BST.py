class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST():
    def __init__(self):
        self.root=None

    def insert(self,data):
        newNode=Node(data)
        curr=self.root
        if self.root is None :
            self.root=newNode
            return
        else:
            while True:
                if data < curr.data:
                    if curr.left is None:
                        curr.left = newNode
                        break

                    else:
                        curr= curr.left  
                elif data >=curr.data:
                    if curr.right is None:
                        curr.right=newNode
                        break
                    else:
                        curr=curr.right  

    def lookup(self,data):
        curr=self.root
        if curr is None :
            print("tree is empty")
            return
        else:
            while curr is not None:
                if data < curr.data:
                    curr=curr.left
                elif data > curr.data:
                    curr=curr.right
                else:
                    print("found in BST")
                    return
            print("Not in BST")
            return   
    def minValueNode(self,node):
        curr=node
        while curr.left is not None:
            curr=curr.left
        return curr 

    def delete(self,currNode:Node,key:int):
        if currNode ==None:
            return currNode   
        elif(key<currNode.data):
            currNode.left=self.delete(currNode.left,key)
        elif (key>currNode.data):
            currNode.right=self.delete(currNode.right,key)
        else:
            if(currNode.left==None):
                temp=currNode.right
                if currNode == self.root:
                    self.root=temp
                    return
                else:    
                     currNode=None    
                     return temp
            elif(currNode.right==None):
                temp=currNode.left
                
                if currNode == self.root:
                    self.root=temp
                    return
                else:    
                     currNode=None    
                     return temp
               
            replaceNode=self.minValueNode(currNode.right)
            currNode.data=replaceNode.data
            currNode.right=self.delete(currNode.right,currNode.data) 
        return currNode                    
    
    def deleteIterative(self,key):
        parent=None
        currNode=self.root
        if self.root == None:
            print("empty BST")
        else:
            while currNode !=None and currNode.data !=  key :
                parent = currNode
                if key<currNode.data:
                    flag=0
                    currNode=currNode.left
                else:
                    currNode=currNode.right
                    flag=1

        if currNode is None:
            print("Node not in BST")
            return
        else:
            if(currNode.left ==None)and(currNode.right == None) :
                if flag:
                    parent.right = None
                else:
                    parent.left =  None
            elif (currNode.left ==None)or(currNode.right == None) :
                if currNode.left is None:
                    if flag:
                        parent.right = currNode.right
                    else:
                        parent.left= currNode.right
                else:
                    if flag:
                        parent.right = currNode.left
                    else:
                        parent.left= currNode.left
            else:
                replaceNode=self.minValueNode(currNode.right)
                self.delete(replaceNode.data)
                currNode.data=replaceNode.data

    def inorder(self,root:Node):
        if root:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)  
          

    def inorderIterative(self,root):
        curr=root
        if root is None:
            return
        s=[]
        while True:
            if curr is not None:
                s.append(curr)
                curr=curr.left
            elif s:
                popItem=s.pop()
                print(popItem.data,end=" ")
                if popItem.right:
                    curr=popItem.right
            else:
                print()
                return        
                    
    def preorder(self,root:Node):
        if root:
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def preorderIterative(self,root:Node):
        if root is None:
            return
        curr = root
        s=[]
        s.append(root)
        while len(s) > 0:
            popItem=s.pop()
            print(popItem.data,end=" ")
            if popItem.right :
                s.append(popItem.right)
            if popItem.left:
                s.append(popItem.left) 
        print()         
        return 

    def postorder(self,root:Node):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")  

    def postorderIterative(self,root:Node):
        curr=root
        s=[]
        while True:
            while curr:
                if curr.right:
                    s.append(curr.right)
                s.append(curr)
                curr=curr.left
            curr=s.pop()
            if curr.right is not None and peek(s) == curr.right:
                s.pop()
                s.append(curr)
                curr=curr.right
            else:
                print(curr.data , end=" ")
                curr=None
            if len(s)<=0:
                print()
                break 
    

    def levelOrderTraversal(self,root:Node):
        if root is None:
            return
        curr=root
        q=[]
        q.append(curr)
        while len(q)>0:
            print(q[0].data , end=" ")
            node= q.pop(0)
            if node.left :
                q.append(node.left)
            if node.right:
                q.append(node.right)   



    def heightRecursive(self,node:Node):
        if node is None:
            return 0

        lheight=self.heightRecursive(node.left)  
        rheight=self.heightRecursive(node.right)

        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1  

    def heightIterative(self,node):
         if node is None:
             return
         s=[]
         s.append(node)
         height=0
         while True:
             if len(s)<=0:
                 return height
             if len(s)>0:
                 height+=1 

             nodeNo=len(s)
             while nodeNo>0:
                 popItem=s.pop(0)
                 if popItem.left:
                     s.append(popItem.left)
                 if popItem.right:
                     s.append(popItem.right)
                 nodeNo-=1     


        
        
              











def peek(s):
    if len(s)>0:
        item=s[-1]
        return item            











              



            



                                    

                                
tree=BST()
a=Node(15)
tree.insert(15)
tree.insert(18)
tree.insert(16)

tree.insert(8)
tree.insert(7)
tree.insert(9)
tree.lookup(15)
tree.lookup(15)
tree.inorder(tree.root)
tree.inorderIterative(tree.root)
tree.preorder(tree.root)
tree.preorderIterative(tree.root)
tree.postorder(tree.root)
tree.postorderIterative(tree.root)
tree.levelOrderTraversal(tree.root)
print()
print(tree.heightRecursive(tree.root))
print(tree.heightIterative(tree.root))











