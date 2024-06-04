class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
        
    def print_stack(self):
        node = self.top
        while node:
            print(node.value)
            node = node.next
        
my_stack = Stack(5)
my_stack.print_stack()