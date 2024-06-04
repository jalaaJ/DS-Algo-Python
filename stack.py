class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
        
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        
    def pop(self):
        node_to_remove = self.top
        if node_to_remove is not None:
            self.top = self.top.next
            node_to_remove.next = None
            self.height -= 1
            return node_to_remove
        else:
            return None
            
        
    def print_stack(self):
        node = self.top
        while node:
            print(node.value)
            node = node.next
        
my_stack = Stack(5)
my_stack.push(10)
my_stack.push(15)
my_stack.pop()
my_stack.print_stack()