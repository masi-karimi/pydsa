# Hash Table implementation (applying two collision resolution techniques: Separate Chaining [Open Hashing] for one & only Linear Probing from the Open Addressing [Closed Hashing] category)

import utility


# 🟥 =====> Hash Table applying the Separate Chaining (Open Hashing) collision resolution technique <=====

# 🎯 The Chaining Hash Table class
class ChainingHashTable:
    def __init__(self, size):
        """
        Initialize the hash table with a given size.
        Each bucket is initialized as an empty list to handle collisions using chaining.
        """
        self.size = size
        self.table = [[] for _ in range(size)]
        print(f"\n✅ Initialized hash table with {size} buckets.")
        print("ℹ️ Since Chaining uses another data structure for collision resolution, the hash table remains dynamic, so you need not worry about storage space!\n")

    def hash_function(self, key):
        """
        Compute the hash value for a given key.
        The hash value is the remainder of the key's hash code divided by the table size.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table.
        If the key already exists, update its value.
        """
        index = self.hash_function(key)
        # Check if the key already exists in the bucket
        for kv in self.table[index]:
            if kv[0] == key:
                kv[1] = value
                return f"\n✅ Insertion successful. Updated key ({key}) with value ({value}) at index {index}."
        # If the key does not exist, append the new key-value pair
        self.table[index].append([key, value])
        return f"\n✅ Insertion successful. Inserted key ({key}) with value ({value}) at index {index}."

    def lookup(self, key):
        """
        Look up the value associated with a given key.
        Return the value if found, otherwise return None.
        """
        index = self.hash_function(key)
        # Search for the key in the bucket
        for kv in self.table[index]:
            # If found ...
            if kv[0] == key:
                return f"\n✅ Searching successful. Key ({key}) found at index {index} with value ({kv[1]})."
                # return kv[1]
        # If not found after looping through all the kvs ...
        return f"\n❌ Searching successful. Key ({key}) not found."
        # return None

    def delete(self, key):
        """
        Delete a key-value pair from the hash table.
        """
        index = self.hash_function(key)
        # Search for the key in the bucket
        for i, kv in enumerate(self.table[index]):
            # If found ...
            if kv[0] == key:
                del self.table[index][i]
                return f"\n✅ Deletion successful. Deleted key ({key}) from index {index}."
        # If not found ...
        return f"\n🚫 Deletion unsuccessful. Key ({key}) not found, nothing to delete."

    def display(self):
        """
        Prints the Chaining Hash Table in a presentable format.
        """
        total_buckets = len(self.table)
        indices = [index for index in range(total_buckets)]
        for bucket in self.table:
            print("🔹", indices.pop(0), bucket)


# 🎯 The Chaining Hash Table Main
def chaining_main():
    
    # 🟢 Starting loop (Going DIY or using the example)
    while True:
        example = input("""\n🛠️ Do you want to create a hash table yourself or use the preloaded example?
●1) Create a hash table
●2) Use the example
>>> """)
        match example:
            
            # Create a hash table
            case "1":
                # Taking & verifying the size input, the only one needed for initializing the hash table
                while True:
                    size = utility.input_verify("int", "the total number of buckets you want; in other words, the size of the hash table")
                    if size is not None:
                        chaining_ht = ChainingHashTable(size)
                        chaining_ht.display()
                        break
                    else:
                        print("\n🚫 Invalid data type. Hash table size must be an INT.")
                        continue
                break
                      
            # Use example
            case "2":
              chaining_ht = ChainingHashTable(5)
              # Directly populating the self.table property not possible here due to the built-in hash() function returning different values at different runs, causing the elements to go into different buckets & totally rendering hard-coded positioning useless!
              chaining_ht.insert("Messi", "10")
              chaining_ht.insert("Apple", 1976)
              chaining_ht.insert(2024, -273.15)
              chaining_ht.insert("UFO", "Roswell, NM")
              # Displaying the example hash table
              print("👇🏻 Here's an example Chaining Hash Table:")
              chaining_ht.display()
              break
                
            # Invalid
            case _:
                print("\n❌ Invalid code number!")
                continue
    
    
    # 🟢 Operation selection loop
    while True:
        opr = input("""\n⚔️ Which operation do you want to perform with the Chaining Hash Table?
★0) Definition
★1) Insertion
★2) Deletion
★3) Searching
★4) Displaying
★5) New Hash Table
★6) New Data Structure
★7) Exiting the Program

>>> """)
        match opr:
         
            # Definition
            case "0":
                hash_table_intro("def")
            
            # Insertion
            case "1":
                key = get_key()
                value = get_value()
                result = chaining_ht.insert(key, value)
                print(result)
            
            # Deletion
            case "2":
                key = get_key(text="key that you want to delete")
                result = chaining_ht.delete(key)
                print(result)
             
            # Searching
            case "3":
                key = get_key(text="key that you want to  search for")
                result = chaining_ht.lookup(key)
                print(result)
            
            # Displaying
            case "4":
                print("\n👇🏻 Here's a display of your Hash Table:")
                chaining_ht.display()
                
            # New Hash Table
            case "5":
                utility.clear()
                hash_table_intro("full")
                hash_table_main()
                break
            
            # New Data Structure
            case "6":
                utility.clear()
                utility.main_intro()
                break
            
            # Exiting the Program
            case "7":
                exit()
            
            # Invalid
            case _:
                print("\n🚫 Invalid operation code!")



# 🟥 =====> Hash Table applying the Linear Probing collision resolution technique from the Open Addressing (Close Hashing) category <=====

# 🎯 The Linear Probing Hash Table class
class LinearProbingHashTable:
    def __init__(self, size):
        """
        Initialize the hash table with a given size.
        Each slot is initialized to None.
        """
        self.size = size
        self.table = [None] * size
        print(f"\n✅ Initialized hash table with {size} slots.")

    def hash_function(self, key):
        """
        Compute the hash value for a given key.
        The hash value is the remainder of the key's hash code divided by the table size.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table.
        If the key already exists, update its value.
        """
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return f"\n✅ Insertion successful. Updated key ({key}) with value ({value}) at index {index}."
            index = (index + 1) % self.size
            if index == original_index:
                return "\n🚫 Insertion unsuccessful. Hash table is full; cannot insert new key."
        self.table[index] = (key, value)
        return f"\n✅ Insertion successful. Inserted key ({key}) with value ({value}) at index {index}."

    def lookup(self, key):
        """
        Look up the value associated with a given key.
        Return the value if found, otherwise return None.
        """
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return f"\n✅ Key ({key}) found at index {index} with value ({self.table[index][1]})."
                # return self.table[index][1]
            index = (index + 1) % self.size
            if index == original_index:
                break
        return f"\n❌ Key ({key}) not found."
        # return None

    def delete(self, key):
        """
        Delete a key-value pair from the hash table.
        """
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                print(f"\n✅ Deletion successful. Deleted key ({key}) from index {index}.")
                # Rehash all elements in the same cluster
                next_index = (index + 1) % self.size
                while self.table[next_index] is not None:
                    rehash_key, rehash_value = self.table[next_index]
                    self.table[next_index] = None
                    print("\n♻️ Rehashing...")
                    self.insert(rehash_key, rehash_value)
                    next_index = (next_index + 1) % self.size
                return
            index = (index + 1) % self.size
            if index == original_index:
                break
        print(f"\n❌ Key ({key}) not found, nothing to delete.")

    def display(self):
        """
        Prints the Chaining Hash Table in a presentable format.
        """
        total_slots = len(self.table)
        indices = [index for index in range(total_slots)]
        for slot in self.table:
            print("🔹", indices.pop(0), slot)


# 🎯 The Linear Probing Hash Table Main
def linear_probing_main():
    
    # 🟢 Starting loop (Going DIY or using the example)
    while True:
        example = input("""\n🛠️ Do you want to create a hash table yourself or use the preloaded example?
●1) Create a hash table
●2) Use the example
>>> """)
        match example:
            
            # Create a hash table
            case "1":
                # Taking & verifying the size input, the only one needed for initializing the hash table
                while True:
                    size = utility.input_verify("int", "the total number of slots you want; in other words, the size of the hash table")
                    if size is not None:
                        linear_probing_ht = LinearProbingHashTable(size)
                        linear_probing_ht.display()
                        break
                    else:
                        print("\n🚫 Invalid data type. Hash table size must be an INT.")
                        continue
                break
                      
            # Use example
            case "2":
              linear_probing_ht = LinearProbingHashTable(5)
              # Directly populating the self.table property not possible here due to the built-in hash() function returning different values at different runs, causing the elements to go into different buckets & totally rendering hard-coded positioning useless!
              linear_probing_ht.insert("Messi", "10")
              linear_probing_ht.insert("Apple", 1976)
              linear_probing_ht.insert(2024, -273.15)
              linear_probing_ht.display()
              break
                
            # Invalid
            case _:
                print("\n❌ Invalid code number!")
                continue
    
    
    # 🟢 Operation selection loop
    while True:
        opr = input("""\n⚔️ Which operation do you want to perform with the Linear Probing Hash Table?
★0) Definition
★1) Insertion
★2) Deletion
★3) Searching
★4) Displaying
★5) New Hash Table
★6) New Data Structure
★7) Exiting the Program

>>> """)
        match opr:
         
            # Definition
            case "0":
                hash_table_intro("def")
            
            # Insertion
            case "1":
                key = get_key()
                value = get_value()
                result = linear_probing_ht.insert(key, value)
                print(result)
            
            # Deletion
            case "2":
                key = get_key(text="key that you want to delete")
                linear_probing_ht.delete(key)
             
            # Searching
            case "3":
                key = get_key(text="key that you want to  search for")
                result = linear_probing_ht.lookup(key)
                print(result)
            
            # Displaying
            case "4":
                print("\n👇🏻 Here's a display of your Hash Table:")
                linear_probing_ht.display()
                
            # New Hash Table
            case "5":
                utility.clear()
                hash_table_intro("full")
                hash_table_main()
                break
            
            # New Data Structure
            case "6":
                utility.clear()
                utility.main_intro()
                break
            
            # Exiting the Program
            case "7":
                exit()
            
            # Invalid
            case _:
                print("\n🚫 Invalid operation code!")



# 🟥 =====> The Hash Table main & intro functions <=====

# 🎯 The Hash Table main function
## Since we have hash tables with two different collision resolution techniques in the program, this main function just does pattern matching to their mains before breaking to transfer the control to the paramount main.py loop (after we break out of the other mains).
def hash_table_main():
    # Summoning the intro
    hash_table_intro("full")
        
    # 🟢 Hash Table Collision Resolution Type Selection loop
    while True:
        hash_table_type = input("""\n🧪 Which type of collision resolution do you want in the hash table?
★1) Separate Chaining (Open Hashing)
★2) Linear Probing (from the Open Addressing [Closed Hashing] category)
>>> """)
    
        match hash_table_type:
            # Chaining
            case "1":
                chaining_main()
                break
                
            # Linear Probing 
            case "2":
                linear_probing_main()
                break
             
            # Invalid
            case _:
                print("\n🚫 Invalid representation type code!")


# 🎁 The Hash Table intro function
def hash_table_intro(condition):
    hash_table_ascii = """\n
.---.  .---.    ____       .-'''-. .---.  .---.         ,---------.    ____     _______     .---.       .-''-.   
|   |  |_ _|  .'  __ `.   / _     \|   |  |_ _|         \          \ .'  __ `. \  ____  \   | ,_|     .'_ _   \  
|   |  ( ' ) /   '  \  \ (`' )/`--'|   |  ( ' )          `--.  ,---'/   '  \  \| |    \ | ,-./  )    / ( ` )   ' 
|   '-(_{;}_)|___|  /  |(_ o _).   |   '-(_{;}_)            |   \   |___|  /  || |____/ / \  '_ '`) . (_ o _)  | 
|      (_,_)    _.-`   | (_,_). '. |      (_,_)             :_ _:      _.-`   ||   _ _ '.  > (_)  ) |  (_,_)___| 
| _ _--.   | .'   _    |.---.  \  :| _ _--.   |             (_I_)   .'   _    ||  ( ' )  \(  .  .-' '  \   .---. 
|( ' ) |   | |  _( )_  |\    `-'  ||( ' ) |   |            (_(=)_)  |  _( )_  || (_{;}_) | `-'`-'|___\  `-'    / 
(_{;}_)|   | \ (_ o _) / \       / (_{;}_)|   |             (_I_)   \ (_ o _) /|  (_,_)  /  |        \\       /  
'(_,_) '---'  '.(_,_).'   `-...-'  '(_,_) '---'             '---'    '.(_,_).' /_______.'   `--------` `'-..-'\n"""
    
    hash_table_def = """\n🎯 A graph is a non-linear data structure consisting of vertices (nodes) and edges that connect pairs of vertices. Graphs are used to model relationships between entities, making them essential in various fields such as computer science, biology, social networks, and transportation. Graphs can be directed or undirected, weighted or unweighted, and can contain cycles or be acyclic. The versatility of graphs allows them to represent complex structures and relationships, enabling efficient problem-solving and analysis. Graphs can be represented using either an Adjacency Matrix or an Adjacency List.

🌟 An adjacency matrix is a 2D array used to represent a graph, where the rows and columns correspond to vertices. The element at row (i) and column (j) indicates the presence and weight of an edge between vertices (i) and (j). For an undirected graph, the matrix is symmetric, while for a directed graph, it is not. The adjacency matrix allows for quick edge lookups with a time complexity of O(1), but it requires O(V^2) space, making it more suitable for dense graphs where the number of edges is close to the maximum possible.

🌟 An adjacency list represents a graph using an array of lists. Each element in the array corresponds to a vertex, and the list at each index contains the vertices adjacent to that vertex. This representation is more space-efficient for sparse graphs, as it only stores existing edges, resulting in a space complexity of O(V + E). Adjacency lists allow for efficient traversal of the graph, making them ideal for algorithms like Depth-First Search (DFS) and Breadth-First Search (BFS). However, edge lookups can be slower compared to an adjacency matrix, with a time complexity proportional to the degree of the vertex."""

    if condition == "full":
        print(hash_table_ascii)
        print(hash_table_def)
    elif condition == "def":
        print(hash_table_def)


# 🎁 The helper functions for getting the key & the value
    
# Key
def get_key(text="key"):
    print("\n🔑 Specify the Key:")
    while True:
        key = utility.input_verify(msg=text)
        if key is None:
            print(f"\n🚫 Invalid data type for the key.")
            continue
        else:
            return key

# Value
def get_value(text="value"):
    print("\n🚪 Specify the Value:")
    while True:
        value = utility.input_verify(msg=text)
        if value is None:
            print(f"\n🚫 Invalid data type for the value.")
            continue
        else:
            return value


# 🎯 Calling the Hash Table main function
if __name__ == "__main__":
    hash_table_main()
