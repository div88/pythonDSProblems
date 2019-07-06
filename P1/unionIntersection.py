class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def add(self, value):
		if self.head == None:
			self.head = Node(value)
		else:
			current = self.head
			while current.next != None:
				current = current.next
			current.next =  Node(value)

	def printList(self):
		listStr = []
		listStr.append(self.head.value)
		current = self.head
		while current.next != None:
			listStr.append(current.next.value)
			current = current.next
		print(listStr)

	def remove(self, value):
		if self.head.value == value:
			self.head = self.head.next
		else:
			current = self.head
			while current != None:
				if(current.next != None and current.next.value == value):
					current.next = current.next.next
				else:
					print("Value is not in the list")
				current = current.next

	def traverse(self):
		listStr = []
		listStr.append(self.head.value)
		current = self.head
		while current.next != None:
			listStr.append(current.next.value)
			current = current.next
		return listStr

	def union(self, list1, list2):
		a = set(sorted(list1.traverse()))
		b = set(sorted(list2.traverse()))
		return a.union(b)

	def intersection(self, list1, list2):
		a = set(sorted(list1.traverse()))
		b = set(sorted(list2.traverse()))
		return a.intersection(b)


list1 = LinkedList();
list1.add(3);
list1.add(2);
list1.add(4);
list1.add(35);
list1.add(6);
list1.add(65);
list1.add(6);
list1.add(4);
list1.add(3);
list1.add(21);
list1.printList();


list2 = LinkedList();
list2.add(6);
list2.add(32);
list2.add(4);
list2.add(9);
list2.add(6);
list2.add(1);
list2.add(11);
list2.add(21);
list2.add(1);
list2.add(21);
list2.printList();

l1 = list1.union(list1, list2)

l2 = list1.intersection(list1, list2)

list3 = LinkedList();
for i in l1:
	list3.add(i)
list4 = LinkedList();
for i in l2:
	list4.add(i)

list3.printList();
list4.printList();


# element_1 = [3,2,4,35,6,65,6,4,3,23]
# element_2 = [1,7,8,9,11,21,1]

# element_1 = [1,1]
# element_2 = [1,1,2,2]

# element_1 = [1,'',3,None]
# element_2 = [1,None]



