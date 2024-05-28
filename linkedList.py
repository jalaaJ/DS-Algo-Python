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
                
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
        
my_linkedlist = LinkedList(5)
print(my_linkedlist.pop())
print(my_linkedlist.pop())
