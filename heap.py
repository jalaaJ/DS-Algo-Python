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
    
    