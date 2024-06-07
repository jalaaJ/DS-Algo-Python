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
    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
    
    def item_in_common(self, list1, list2):
        for item1 in list1:
            for item2 in list2:
                if item1 == item2:
                    return True
        return False
    
    def item_in_common_optimal(self, list1, list2):
        my_dict = {}
        for item in list1:
            my_dict[item] = True
        for item in list2:
            if item in my_dict:
                return True
        return False
        
    def print_hashtable(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
          
hash_table = HashTable(7)
hash_table.set_item("bolts", 123)
hash_table.set_item("washers", 321)
print(hash_table.get_item("lumber"))
hash_table.print_hashtable()
list1 = [1, 2, 3]
list2 = [4, 5, 3]
print(hash_table.item_in_common(list1, list2))
print(hash_table.item_in_common_optimal(list1, list2))
