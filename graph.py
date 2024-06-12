class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False
    
    def add_edge(self, vertex1, vertex2):
        if self.vertices_exist(vertex1, vertex2):
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False
    
    def remove_edge(self, vertex1, vertex2):
        if self.vertices_exist(vertex1, vertex2):
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        return False
    
    def vertices_exist(self, vertex1, vertex2):
        return vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys()

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, ": ", self.adjacency_list[vertex])
            
my_graph = Graph()
my_graph.add_vertex("JJ")
my_graph.add_vertex("Jomana")
my_graph.add_edge("JJ", "Jomana")
my_graph.remove_edge("JJ", "J")
my_graph.print_graph()
    