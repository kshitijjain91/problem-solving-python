# Implementing a stack data structure using lists as the primitive data type
# It will create a stack with some elements, push elements into it, can peek at the top element etc.

class Stack():

	def __init__(self):
		self.element_lst = []

	def is_empty(self):
		return len(self.element_lst) == 0

	def length(self):
		return len(self.element_lst)

	def push(self, element):
		self.element_lst.insert(0, element)
		return self.element_lst

	def pop(self):
		return self.element_lst.pop(0) 

	def peek(self):
		return(self.element_lst[0])

stack1 = Stack()

print(stack1.peek())