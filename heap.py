class MaxHeap:
    def __init__(self):
        self.heap = []
        
    # Helper methods:
    
    def _left_child_index(self, index):
        return 2 * index - 1
    
    def _right_child_index(self, index):
        return 2 * index + 2
    
    def _parent_index(self, index):
        return (index - 1) // 2
    
    def _swap_values(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
        
    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1
        while current > 0 and self.heap[current] > self.heap[self._parent_index(current)]:
            self._swap_values(current, self._parent_index(current))
            current = self._parent_index(current)

myHeap = MaxHeap()
myHeap.insert(99)
myHeap.insert(72)
myHeap.insert(61)   
myHeap.insert(58)

print(myHeap.heap)

myHeap.insert(100)

print(myHeap.heap)