import sys


def runHuffman(str):
    map = frequencyCounter(str)
    pQueue = PriorityQueue()

    for key in map:
        value = map[key]
        pQueue.enqueue(value, key, None, None)
    
    
    while pQueue.size > 1:
        first = pQueue.dequeue();
        second = pQueue.dequeue();
        pQueue.enqueue(first.priority + second.priority, '0', first, second)

    root = pQueue.dequeue()
    huffmanMap = {}
    encodeHuffman(root, "", huffmanMap);
   
    print ("The size of the data is: {}\n".format(sys.getsizeof(str)))
    print ("The content of the data is: {}\n".format(str))

    encoded = [];
    for s in str:
        encoded.append(huffmanMap.get(s))

    e = ''.join(encoded)

    if len(e) > 0:
        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(e, base=2))))
        print ("The content of the encoded data is: {}\n".format(e))
    else:
        print("The size of string is empty")

    output = [];
    indexObj = { 'index': -1 }
    encodedString = ''.join(encoded)
    while indexObj['index'] < len(encodedString) - 2:
        decodeHuffman(root, indexObj, encodedString, output)

    d = ''.join(output)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(d)))
    print ("The content of the decoded data is: {}\n".format(d))

def decodeHuffman(node, indexObj, encodedString, output):
    if node != None:
        if node.left == None and node.right == None:
            output.append(node.ch);
            return
        indexObj['index'] += 1
        if encodedString[indexObj['index']] == '0':
            decodeHuffman(node.left, indexObj, encodedString, output)
        else:
            decodeHuffman(node.right, indexObj, encodedString, output)
        

def encodeHuffman(node, str, map):
    if node != None:
        if node.left == None and node.right == None:
            map[node.ch] = str

        encodeHuffman(node.left, str + "0", map)
        encodeHuffman(node.right, str + "1", map)

def frequencyCounter(str):
    map = {}

    for el in str:
        if map.get(el) != None:
            count = map.get(el);
            count += 1
            map[el] = count;
        else:
            map[el] = 1;

    return map

class PriorityQueueNode:
    def __init__(self,priority,ch,left,right):
        self.priority = priority;
        self.ch = ch
        self.next = None
        self.left = left
        self.right = right

class PriorityQueue:
    def __init__(self):
        self.head = None
        self.size = 0

    def enqueue(self,priority, ch, left, right):
        if self.head == None:
            self.head = PriorityQueueNode(priority, ch, left, right)
            self.size += 1
        else:
            curr = self.head;
            if curr.priority > priority:
                self.head = PriorityQueueNode(priority, ch, left, right)
                self.head.next = curr
            else:
                placed = False;
                while curr.next != None:
                    if curr.next.priority > priority:
                        temp = curr.next;
                        curr.next = PriorityQueueNode(priority, ch, left, right)
                        curr.next.next = temp
                        placed = True
                        break;
                    curr = curr.next

                if placed == False:
                    curr.next = PriorityQueueNode(priority, ch, left, right)
            self.size += 1;

    def dequeue(self):
        if self.head == None:
            print("Queue empty")
        else:
            curr = self.head
            if self.size == 1:
                self.head = None
            else:
                self.head = self.head.next
            self.size -= 1
            return curr


# TestCases
runHuffman("The bird is the word")
runHuffman("This is")
runHuffman("")



