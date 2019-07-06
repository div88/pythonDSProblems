class Node:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.next = None
        # self.prev = None


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.itemlist = {}
        self.count = 0
        self.head = None


    def set(self, k, v):
        if self.count >= 5: 
            if self.itemlist.get(k) == None:
                self.remove()
                self.itemlist.pop(self.head.value, None)
            
            self.addValue(k,v)
            print(self.itemlist) #prints dictionary

        else:
            self.addValue(k,v)

    def addValue(self, ke, va):
        if self.itemlist.get(ke):
            
            self.itemlist[ke] = va
            self.updateList(ke,va)
        else: 
            self.itemlist[ke] = va
            
            self.count += 1
            

            if self.head == None:
                self.head = Node(ke,va)
            else:
                current = self.head
                while current.next != None:
                    current = current.next
                
                current.next = Node(ke,va)

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if self.itemlist.get(key) != None:
            print(f'Found {key}')
            val = self.itemlist.get(key)
            self.updateList(key, val)
        else:
            print(-1)

    def updateList(self, key, value):
        if self.head.key == key:
            temp = self.head
            self.head =  self.head.next
            current = self.head
            while current.next != None:  
                current = current.next
            tail = current
            tail.next = Node(temp.key, value)
            # self.printl()
        else:
            current = self.head
            while current.next != None:  
                if current.next.key == key:
                    temp = current.next
                    current.next = current.next.next;
                current = current.next
            tail = current
            tail.next = Node(temp.key, value)
            # self.printl()  

    def remove(self):
        if self.head != None:
            self.head = self.head.next
            # self.printl()
      


    def printl(self):
        liststr = []
        current = self.head
        while current != None:
            
            liststr.append({current.key : current.value})
            current = current.next

        print(liststr)
        



our_cache = LRU_Cache(5)

our_cache.set(1,1)
our_cache.set(2,2)
our_cache.set(3,3)
our_cache.set(4,4)
our_cache.set(5,5)
our_cache.set(4,28)

our_cache.printl()
our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(7)       # return -1

our_cache.set(6,6)



# our_cache1 = LRU_Cache(5)

# our_cache1.set(1, 0)
# our_cache1.set(2, '')
# our_cache1.set('', '')
# our_cache1.set(None, None)
# our_cache1.get('')   
# our_cache1.get(None)    
# our_cache1.get(5)       # return -1




