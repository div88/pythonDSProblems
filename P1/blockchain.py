import hashlib
import datetime
from string import Template

class Block:
    def __init__(self, data, previous_hash):
      self.timestamp = self.timestamp()
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(data)

    def calc_hash(self, str):
      sha = hashlib.sha256()
      if str:
      	hash_str = str.encode('utf-8')
      else:
      	newStr = "None" + self.timestamp
      	hash_str = newStr.encode('utf-8')
      sha.update(hash_str)

      return sha.hexdigest()

    def timestamp(self):
      dt = datetime.datetime.utcnow()
      tstamp = dt.strftime("%H:%M %m/%d/%Y")
      return tstamp

class BlockChain:
	def __init__(self):
		self.head = None
		self.chain = []


	def add(self, dat):
		if self.head == None:
			prevhash = 0
			self.head = Block(dat, prevhash)
			self.chain.append(self.head)
		else:
			current = self.head
			prevhash = self.head

			if len(self.chain) >= 1:
				prev = self.chain[len(self.chain)-1]
				current =  Block(dat, prev.hash)
				self.chain.append(current)

	def printList(self):
		print('-----------------------')
		for i in self.chain:
			print(f'Timestamp: {i.timestamp}')
			print(f'Data: {i.data}')
			print(f'SHA256 Hash: {i.hash}')
			print(f'Prev-Hash: {i.previous_hash}')
			print('-----------------------')


# Test Cases


bc1 = BlockChain()

bc1.add("Block0 Data")
bc1.add("Block1 Data")
bc1.add("Block2 Data")
bc1.add("Block3 Data")
bc1.printList()

# ********************************

bc2 = BlockChain()

bc2.add("Block1")
bc2.add("  ")
bc2.add(None)

bc2.printList()

# ********************************
bc2 = BlockChain()

bc2.add("")
bc2.add("  ")
bc2.add(None)
bc2.printList()


