from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()
        self.wordList = []
        
    def makeTrie(self,words):
        for word in words:
            self.insert(word)

    def insert(self, word):
        ## Add a word to the Trie
        currentNode = self.root
        
        for w in list(word):
            if not currentNode.children.get(w):
                currentNode.children[w] = TrieNode()
            
            currentNode = currentNode.children[w]
        
        currentNode.endOfWord = True
                

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        currentNode = self.root
        found = True
        
        for char in list(prefix):
            if not currentNode.children(char):
                found = False
                break
                
            currentNode = currentNode.children[char]
        
        return currentNode and currentNode.endOfWord and found

    def suggRec(self, node, word):
        if node.endOfWord:
            self.wordList.append(word)
            
        for a,n in node.children.items():
            self.suggRec(n, word + a)

    def printAutoSugg(self, key):
        node = self.root
        not_found = False
        temp_word = ''

        for a in list(key):
            if not node.children.get(a):
                not_found = True
                break
                
            temp_word += a
            node = node.children[a]
            
        if not_found:
            return 0
        elif node.endOfWord and not node.children:
            return -1
        
        self.wordList = []
        self.suggRec(node, temp_word)
        
        for s in self.wordList:
            s.replace(temp_word,'')
            print(s.replace(temp_word,''))
        
        return 1

## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.endOfWord = False
        self.children = {}
    
#     def insert(self, char):
#         ## Add a child node in this Trie
       

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
# for word in wordList:
MyTrie.makeTrie(wordList)
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.printAutoSugg(prefix)
        if prefixNode:
            print()
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');