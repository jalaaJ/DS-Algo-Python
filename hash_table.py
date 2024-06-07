class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size
        
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
        
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    value = self.data_map[index][i][1]
                    return value
        return None
        
    def print_hashtable(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
          
hash_table = HashTable(7)
hash_table.set_item("Jalaa", 123)
hash_table.set_item("Jomana", 321)
print(hash_table.get_item("Jomana"))
