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
        
    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child_index(index)
            right_index = self._right_child_index(index)
            if (left_index < len(self.heap)) and self.heap[left_index] > self.heap[max_index]:
                max_index = left_index
            if (right_index < len(self.heap)) and self.heap[right_index] > self.heap[max_index]:
                max_index = right_index
            if max_index != index:
                self._swap_values(max_index, index)
                index = max_index
            else:
                return
        
            
        
    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1
        while current > 0 and self.heap[current] > self.heap[self._parent_index(current)]:
            self._swap_values(current, self._parent_index(current))
            current = self._parent_index(current)
            
    def remove(self):
        if len(self.heap) == 0:
            return None
        elif len(self.heap) == 1:
            return self.heap.pop()
        else:
            max_value = self.heap[0]
            self.heap[0] = self.heap.pop()
            self._sink_down(0)
            return max_value

myHeap = MaxHeap()
myHeap.insert(99)
myHeap.insert(72)
myHeap.insert(61)   
myHeap.insert(58)

print(myHeap.heap)

myHeap.insert(100)

print(myHeap.heap)

