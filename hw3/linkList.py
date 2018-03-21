from node import Node

class LinkList:
	def __init__(self) :
			self.head = None

	def append(self, coefficient, power) :
		node = Node(coefficient, power)
		if self.head == None :
			self.head = node
		else :
				node.next = self.head
				#node.next.prev = node
				self.head = node
"""	def print(self):
		while not self.head == None:
			print("coefficient is {}".format(self.head.coefficient))
        	print("power is {}".format(self.head.power))
            self.head = self.head.next """
