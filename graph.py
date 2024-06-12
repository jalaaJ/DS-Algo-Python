class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        self.adjacency_list[vertex] = []
    
    