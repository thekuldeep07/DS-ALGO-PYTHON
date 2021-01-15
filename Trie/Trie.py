class TrieNode:
    def __init__(self,val):
        self.val=val
        self.children={}
        self.endHere=False
class Trie:
    def __init__(self):
        self.root=TrieNode(None)

    def insert(self,word):
        parent=self.root
        for i,char in enumerate(word):
            if char not in parent.children:
                parent.children[char]=TrieNode(char)
            parent=parent.children[char]
            if i == len(word)-1:
                parent.endHere=True    
    def search(self,word):
        parent=self.root
        for char in word:
            if char not in parent.children:
                return False
            parent=parent.children[char]
        return parent.endHere

    def findPrefix(self,prefix):
        parent=self.root 
        for char in prefix:
            if char not in parent.children:
                return False
            parent=parent.children
        return True           


trie1=Trie()
trie1.insert("kuldeep")
print(trie1.search(("kuldeepf")))
