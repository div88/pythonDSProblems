class RouteTrieNode:
    def __init__(self):
        self.key = None
        self.value = None
        self.endOfPath = False
        self.children = {}

class RouteTrie:
    def __init__(self):
        self.root = RouteTrieNode()

    def insert(self, path, value):
        currentPath = path
        currentNode = self.root
        while len(currentPath) > 0:
            if currentPath[0] in currentNode.children:
                currentNode = currentNode.children[currentPath[0]]
                currentPath = currentPath[1:]
            else:
                newNode = RouteTrieNode()
                newNode.key = currentPath[0]
                if len(currentPath) == 1:
                    newNode.value = value
                currentNode.children[currentPath[0]] = newNode
                currentNode = newNode
                currentPath = currentPath[1:]

    def search(self, path):
        currentPath = path
        currentNode = self.root
        while len(currentPath) > 0:
            if currentPath[0] in currentNode.children:
                currentNode = currentNode.children[currentPath[0]]
                currentPath = currentPath[1:]
            else:
                return "Not found handler"
        # print(currentNode.value)
        if currentNode.value == None:
            return "Not found handler"

        return currentNode.value

    def printAllNodes(self):
        nodes = [self.root]
        while len(nodes) > 0:
            for letter in nodes[0].children:
                nodes.append(nodes[0].children[letter])
            # print(nodes.pop(0).key)

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        trie = RouteTrie()

    def add_handler(paths):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        trie = RouteTrie()
        for path, value in paths.items():
            trie.insert(path, value)
        return trie

    def lookup(path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if path.endswith("/") and len(path) > 1:
            trimpath = path[:-1]
        else:
            trimpath = path
        if trie.search(trimpath) == None:
            print(f'{path} = Not found handler')
        else:
            print(f'{path} = {trie.search(trimpath)}')

    # def split_path(self):
    #     # you need to split the path into parts for 
    #     # both the add_handler and loopup functions,
    #     # so it should be placed in a function here



trie = Router()
paths = [{'/': "root", '/home/about': "about handler", '/home/about/me': "me", '/home/contact': "contact handler"}]
trie = Router.add_handler(paths[0])


Router.lookup('/home/about')
Router.lookup('/home/about/')
Router.lookup('/home/about/me')
Router.lookup('/home/contact')
Router.lookup('/')
Router.lookup('/home/')




