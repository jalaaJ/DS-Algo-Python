class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def is_index_not_valid(self, index):
        if index < 0 and index >= self.length:
            return False
        
    # We're returning a boolean value because we will use it in another method    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        to_delete_node = self.tail
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            to_delete_node.prev = None
        self.length -= 1
        return to_delete_node
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        to_delete_node = self.head
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            to_delete_node.next = None
        self.length -= 1
        return to_delete_node
    
    def get(self, index):
        self.is_index_not_valid(index)
        if index < self.length/2:
            node = self.head
            for _ in range(index):
                node = node.next
        else:
            node = self.tail
            for _ in range(self.length - 1, index, -1):
                node = node.prev
        return node
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
my_d_linkedlist = DoublyLinkedList(0)
my_d_linkedlist.append(1)
my_d_linkedlist.append(2)
my_d_linkedlist.append(3)
print(my_d_linkedlist.get(1))
print(my_d_linkedlist.get(2))

