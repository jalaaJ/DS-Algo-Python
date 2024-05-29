class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def append(self, value):
        new_node = Node(value)
        if self.length >= 1:
            self.tail.next = new_node
            self.tail = new_node
            
        else:
            self.head = new_node
            self.tail = new_node
            
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp.value
        else:
            temp = self.head
            prev = self.head
            while temp.next:
                prev = temp
                temp = temp.next
            self.tail = prev
            self.tail.next = None
            self.length -= 1
            return temp.value
        
    def prepend(self, value):
            new_node = Node(value)
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head = new_node
            self.length += 1
            return True
        
    def pop_first(self):
        if self.length == 0:
            return None
        node = self.head  
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            self.head = self.head.next
            self.length -= 1
        node.next = None
        return node.value
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        node = self.head
        for _ in range(index):
            node = node.next
        return node
            
    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return None
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False
        
                
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
        
my_linkedlist = LinkedList(5)
my_linkedlist.prepend(4)
my_linkedlist.prepend(3)
my_linkedlist.pop()
my_linkedlist.pop()
my_linkedlist.pop()
my_linkedlist.prepend(5)
my_linkedlist.prepend(2)
my_linkedlist.pop_first()
my_linkedlist.set_value(0, 10)
my_linkedlist.set_value(0, 100)
my_linkedlist.print_list()
