class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
        
    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        
    def dequeue(self):
        node_to_remove = self.first
        if self.length == 0:
            return None
        elif self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            node_to_remove.next = None
        self.length -= 1
        return node_to_remove
    
    def print_queue(self):
        node = self.first
        while node is not None:
            print(node.value)
            node = node.next
    
my_queue = Queue(5)
my_queue.enqueue(6)
my_queue.enqueue(7)
my_queue.dequeue()
my_queue.print_queue()
