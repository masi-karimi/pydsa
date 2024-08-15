# Graph implementation (Directed Weighted Graph using both Adjacency Matrix & Adjacency List)

import utility

# 🆙 No edge while removal

# 🟥 =====> Adjacency Matrix Directed Weighted Graph <=====

# 🎯 The Adjacency Matrix class
class MatrixDirectedWeightedGraph:
    def __init__(self, num_vertices):
        """
        Initializes the graph with a given number of vertices
        """
        self.num_vertices = num_vertices
        # Create an adjacency matrix initialized to 0
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v, weight):
        # Check if u and v are within the valid range of vertices
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            # Add a directed edge from vertex u to vertex v with the given weight
            self.adj_matrix[u][v] = weight
            print(f"\n✅ Edge addition successful. Edge added from vertex {u} to {v} with weight {weight}.")
        else:
            print(f"\n🚫 Edge addition unsuccessful. Invalid vertices: {u}, {v}.\nValid vertices are in the range 0 to {self.num_vertices - 1}.")

    def remove_edge(self, u, v):
        # Check if u and v are within the valid range of vertices
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            # Remove the edge from vertex u to vertex v by setting the weight to 0
            self.adj_matrix[u][v] = 0
            print(f"\n✅ Edge removal successful. Edge removed from vertex {u} to {v}.")
        else:
            print(f"\n🚫 Edge removal unsuccessful. Invalid vertices: {u}, {v}.\nValid vertices are in the range 0 to {self.num_vertices - 1}.")

    def add_vertex(self):
        # Increment the number of vertices
        self.num_vertices += 1
        # Add a new row at the end of the matrix, initialized to 0
        for row in self.adj_matrix:
            row.append(0)
        # Add a new column at the end of each existing row, also initialized to 0
        self.adj_matrix.append([0] * self.num_vertices)
        print(f"\n✅ Vertex addition successful. Vertex {self.num_vertices - 1} added.")

    def remove_vertex(self, v):
        # Check if the vertex is within the valid range
        if 0 <= v < self.num_vertices:
            # Remove the row corresponding to the vertex
            self.adj_matrix.pop(v)
            # Remove the column corresponding to the vertex
            for row in self.adj_matrix:
                row.pop(v)
            # Decrement the number of vertices
            self.num_vertices -= 1
            print(f"\n✅ Vertex removal successful. Vertex {v} removed.")
        else:
            print(f"\n🚫 Vertex removal unsuccessful. Invalid vertex: {v}.\nValid vertices are in the range 0 to {self.num_vertices - 1}.")

    def dfs_util(self, v, visited):
        # Mark the current node as visited and print it
        visited[v] = True
        print(v, end=' ')
        
        # Recur for all the vertices adjacent to this vertex
        for i in range(self.num_vertices):
            if self.adj_matrix[v][i] != 0 and not visited[i]:
                self.dfs_util(i, visited)

    def dfs(self, start_vertex):
        # Check if the vertex is within the valid range
        if 0 <= start_vertex < self.num_vertices:
            # Initialize all vertices as not visited
            visited = [False] * self.num_vertices
            # Call the recursive helper function to print DFS traversal
            self.dfs_util(start_vertex, visited)
            print("\nℹ️ DFS Traversal") # Adds a newline & traversal type after the output
        else:
            print(f"\n🚫 DFS traversal unsuccessful. Invalid vertex: {start_vertex}.\nValid vertices are in the range 0 to {self.num_vertices - 1}.")

    def bfs(self, start_vertex):
        # Check if the vertex is within the valid range
        if 0 <= start_vertex < self.num_vertices:
            # Initialize all vertices as not visited
            visited = [False] * self.num_vertices
            # Create a queue for BFS
            queue = []
            # Mark the start vertex as visited and enqueue it
            queue.append(start_vertex)
            visited[start_vertex] = True
    
            while queue:
                # Dequeue a vertex from the queue
                v = queue.pop(0)
                print(v, end=' ')
    
                # Get all adjacent vertices of the dequeued vertex v
                # If an adjacent vertex has not been visited, mark it visited and enqueue it
                for i in range(self.num_vertices):
                    if self.adj_matrix[v][i] != 0 and not visited[i]:
                        queue.append(i)
                        visited[i] = True
            print("\nℹ️ BFS Traversal") # Adds a newline & traversal type after the output
        else:
            print(f"\n🚫 DFS traversal unsuccessful. Invalid vertex: {start_vertex}.\nValid vertices are in the range 0 to {self.num_vertices - 1}.")

    def search_edge(self, u, v):
        # Check if there is an edge from vertex u to vertex v
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            result = self.adj_matrix[u][v] != 0
            if result is True:
                weight = self.adj_matrix[u][v]
                print(f"\n✅ Edge searching successful. Edge with weight {weight} found from vertex {u} to {v}.")
            else:
                print(f"\n❌ Edge searching successful. No edge found from vertex {u} to {v}.")
        else:
            print(f"\n🚫 Edge searching unsuccesful. Invalid vertices: {u}, {v}.\nValid vertices are in the range 0 to {self.num_vertices - 1}.")
    
    def display(self):
        total_rows = len(self.adj_matrix)
        indices = [index for index in range(total_rows)]
        for row in self.adj_matrix:
            print("🔹", indices.pop(0), row)
            # print("🔹", self.adj_matrix.index(row), row) => Falsely repeating if two rows happen to be entirely the same


# 🎯 The Adjacency Matrix main function
def adj_matrix_main():
    print("\nℹ️ This program implements a Directed Weighted Graph through the Adjacency Matrix representation. If an unweighted graph is desired, the weights can be simply set to 1.")
    
    # 🟢 Starting loop (Going DIY or using the example)
    while True:
        example = input("""\n🛠️ Do you want to create an Adjacency Matrix graph yourself or use the preloaded example?
●1) Create an Adjacency Matrix Graph
●2) Use the example
>>> """)
        match example:
            
            # Create an Adj Matrix Graph
            case "1":
                while True:
                    num_vertices = utility.input_verify("int", "total number of vertices you want in the Adjacency Matrix")
                    if num_vertices != None:
                        adj_matrix = MatrixDirectedWeightedGraph(num_vertices)
                        print(f"\n👇🏻 Here's your Adjacency Matrix with {num_vertices} vertices:")
                        adj_matrix.display()
                        print(f"\n⚠️ Keep in mind that the vertices are identified with integers in the range zero to number of vertices minus 1, which means 0 to {num_vertices - 1} as of now.")
                        break
                    else:
                        print("\n🚫 The number of vertices can only be an INT.")
                        continue
                break
                      
            # Use example
            case "2":
              adj_matrix = MatrixDirectedWeightedGraph(4)
              # Directly populating the adj_matrix property of the object rather than using add_edge() in a bid to avoid the feedback print statements, as the vertices are identified by index, it's much like automatically adding edges.
              adj_matrix.adj_matrix = [[10,0,30,19], [17,22,37,0], [0,672,8,45], [0,0,0,0]]
              print("\n👇🏻 Here's an example Adjacency Matrix with 4 vertices:")
              adj_matrix.display()
              print(f"\n⚠️ Keep in mind that the vertices are identified with integers in the range zero to number of vertices minus 1, which means 0 to 3 as of now.")
              break
                
            # Invalid
            case _:
                print("\n❌ Invalid code number!")
                continue
    
    
    # 🟢 Operation selection loop
    while True:
        opr = input("""\n⚔️ Which operation do you want to perform with the Adjacency Matrix Graph?
★0) Definition
★1) Adding a Vertex
★2) Removing a Vertex
★3) Adding an Edge
★4) Removing an Edge
★5) Searching an Edge
★6) Traversals
★7) Displaying
★8) New Graph
★9) New Data Structure
★10) Exiting the Program

>>> """)
        match opr:
         
            # Definition
            case "0":
                graph_intro("def")
            
            # Adding a Vertex
            case "1":
                adj_matrix.add_vertex()
                adj_matrix.display()
            
            # Removing a Vertex
            case "2":
                u = get_u(msg="vertex that you want to remove")
                adj_matrix.remove_vertex(u)
                adj_matrix.display()
            
            
            # Adding an Edge
            case "3":
                # Calling the helper functions to get the three needed inputs for edge addition
                u = get_u()
                v = get_v()
                weight = get_weight()
                # Adding the edge after bringing together all the necessary inputs
                adj_matrix.add_edge(u, v, weight)
                adj_matrix.display()
                
                
            # Removing an Edge
            case "4":
                # Gathering the inputs, only vertices this time
                u = get_u()
                v = get_v()
                # Removing the edge
                adj_matrix.remove_edge(u, v)
                adj_matrix.display()
            
            
            # Searching an Edge
            case "5":
                u = get_u()
                v = get_v()
                adj_matrix.search_edge(u, v)
                
                
            # Traversals
            case "6":
               
               # Traversal type selection loop
               while True:
                   traversal_type = input("""\n🗂️ Which traversal do you want?
●1) BFS (Breadth-First Search)
●2) DFS (Depth-First Search)
>>> """)
                   match traversal_type:
                       # BFS
                       case "1":
                           start_vertex = get_u(msg="starting vertex for the BFS")
                           print("\n👉🏻 ", end="")
                           adj_matrix.bfs(start_vertex)   
                           break
                       
                       # DFS
                       case "2":
                           start_vertex = get_u(msg="starting vertex for the DFS")
                           print("\n👉🏻 ", end="")
                           adj_matrix.dfs(start_vertex)
                           break    
                       # Invalid
                       case _:
                           print("\n❌ Invalid code number!")
                           continue

            
            # Displaying
            case "7":
                print("\n👇🏻 Here's your Adjacency Matrix:")
                adj_matrix.display()
                
                
            # New Graph
            case "8":
                utility.clear()
                graph_intro("full")
                graph_main()
                break
            
            
            # New Data Structure
            case "9":
                utility.clear()
                utility.main_intro()
                break
            
            
            # Exiting the Program
            case "10":
                exit()
            
            
            # Invalid
            case _:
                print("\n🚫 Invalid operation code!")



# 🟥 =====> Adjacency List Directed Weighted Graph <=====

# 🎯 The Adjacency List class
class ListDirectedWeightedGraph:
    def __init__(self):
        # Initialize the graph with an empty dictionary. This dictionary has each vertex as a key & a list of all (neighbor, weight) tuples the vertex connects to as the value.
        self.adj_list = {}
        print("\n✅ Adjacency List successfully initialized.")

    def add_vertex(self, vertex):
        # Add a vertex to the graph
        if vertex not in self.adj_list:
            # Adding the vertex as a key & initialzing an empty list as its value
            self.adj_list[vertex] = []
            print(f"\n✅ Vertex addition successful. Vertex {vertex} added.")
        else:
            print(f"\n🚫 Vertex addition unsuccessful Vertex {vertex} already exists.")

    def remove_vertex(self, vertex):
        # Remove a vertex and all its edges
        if vertex in self.adj_list:
            # Remove all edges to this vertex
            for u in self.adj_list:
                self.adj_list[u] = [edge for edge in self.adj_list[u] if edge[0] != vertex]
            # Remove the vertex itself
            del self.adj_list[vertex]
            print(f"\n✅ Vertex removal successful. Vertex {vertex} removed.")
        else:
            print(f"\n🚫 Vertex removal unsuccessful. Vertex {vertex} does not exist.")

    def add_edge(self, u, v, weight):
        # Add a directed edge from vertex u to vertex v with the given weight
        if u in self.adj_list and v in self.adj_list:
            for (neighbor, _weight) in self.adj_list[u]:
                if neighbor == v:
                    self.adj_list[u].remove((neighbor, _weight))
                    break
            self.adj_list[u].append((v, weight))
            print(f"\n✅ Edge addition successful. Edge added from {u} to {v} with weight {weight}.")
        else:
            print(f"\n🚫 Edge addition unsuccessful. One or both vertices {u}, {v} do not exist.")

    def remove_edge(self, u, v):
        # Remove the edge from vertex u to vertex v
        if u in self.adj_list and v in self.adj_list:
            self.adj_list[u] = [edge for edge in self.adj_list[u] if edge[0] != v]
            print(f"\n✅ Edge removal successful. Edge removed from {u} to {v}.")
        else:
            print(f"\n🚫 Edge removal unsuccessful. One or both vertices {u}, {v} do not exist.")

    def dfs_util(self, v, visited):
        # Utility function for DFS traversal
        visited.add(v)
        print(v, end=' ')
        for neighbor, _ in self.adj_list[v]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, start_vertex):
        # Perform DFS traversal starting from the given vertex
        visited = set()
        self.dfs_util(start_vertex, visited)
        print("\nℹ️ DFS Traversal") # Adds a newline & traversal type after the output

    def bfs(self, start_vertex):
        # Perform BFS traversal starting from the given vertex
        visited = set()
        queue = [start_vertex]
        visited.add(start_vertex)

        while queue:
            v = queue.pop(0)
            print(v, end=' ')
            for neighbor, _ in self.adj_list[v]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        print("\nℹ️ BFS Traversal") # Adds a newline & traversal type after the output

    def search_edge(self, u, v):
        # Check if there is an edge from vertex u to vertex v
        if u in self.adj_list:
            for neighbor, weight in self.adj_list[u]:
                if neighbor == v:
                    print(f"\n✅ Edge searching successful. Edge found from {u} to {v} with weight {weight}.")
                    return True
            print(f"\n❌ Edge searching successful. No edge found from {u} to {v}.")
            return False
        else: 
            print(f"\n🚫 Edge searching unsuccessful. Vertex {u} does not exist.")

    def display(self):
        for vertex in self.adj_list:
            print("🔹", vertex, self.adj_list[vertex])


# 🎯 The Adjacency List main function
def adj_list_main():
    print("\nℹ️ This program implements a Directed Weighted Graph through the Adjacency List representation. If an unweighted graph is desired, the weights can be simply set to 1.")
    
    # 🟢 Starting loop (Going DIY or using the example)
    while True:
        example = input("""\n🛠️ Do you want to create an Adjacency List graph yourself or use the preloaded example?
●1) Create an Adjacency List Graph
●2) Use the example
>>> """)
        match example:
            
            # Create an Adj List Graph
            case "1":
                adj_list = ListDirectedWeightedGraph()
                print("\n⚠️ Make sure to add vertices through operation #1 before going for other operations.")
                break
                      
            # Use example
            case "2":
              adj_list = ListDirectedWeightedGraph()
              # Directly populating the adj_list property of the object rather than using add_edge() in a bid to avoid the feedback print statements
              adj_list.adj_list = {0: [(0,10), (2,30), (3,19)], 1: [(0,17), (1,22), (2,37)], 2: [(1,672), (2,8), (3,45)], 3: []}
              print("\n👇🏻 Here's an example Adjacency List Graph:")
              adj_list.display()
              break
                
            # Invalid
            case _:
                print("\n❌ Invalid code number!")
                continue
    
    
    # 🟢 Operation selection loop
    while True:
        opr = input("""\n⚔️ Which operation do you want to perform with the Adjacency List Graph?
★0) Definition
★1) Adding a Vertex
★2) Removing a Vertex
★3) Adding an Edge
★4) Removing an Edge
★5) Searching an Edge
★6) Traversals
★7) Displaying
★8) New Graph
★9) New Data Structure
★10) Exiting the Program

>>> """)
        match opr:
         
            # Definition
            case "0":
                graph_intro("def")
            
            
            # Adding a Vertex
            case "1":
                # Calling the helper function to get input for vertex addition
                u = get_u(msg="vertex that you want to add")
                adj_list.add_vertex(u)
                adj_list.display()
            
            
            # Removing a Vertex
            case "2":
                u = get_u(msg="vertex that you want to remove")
                adj_list.remove_vertex(u)
                adj_list.display()
            
            
            # Adding an Edge
            case "3":
                u = get_u()
                v = get_v()
                weight = get_weight()
                adj_list.add_edge(u, v, weight)
                adj_list.display()
                
                
            # Removing an Edge
            case "4":
                u = get_u()
                v = get_v()
                adj_list.remove_edge(u, v)
                adj_list.display()


            # Searching an Edge
            case "5":
                u = get_u()
                v = get_v()
                adj_list.search_edge(u, v)
                
                
            # Traversals
            case "6":
               
               # Traversal type selection loop
               while True:
                   traversal_type = input("""\n🗂️ Which traversal do you want?
●1) BFS (Breadth-First Search)
●2) DFS (Depth-First Search)
>>> """)
                   match traversal_type:
                       # BFS
                       case "1":
                           start_vertex = get_u(msg="starting vertex for the BFS")
                           print("\n👉🏻 ", end="")
                           adj_list.bfs(start_vertex)   
                           break
                       
                       # DFS
                       case "2":
                           start_vertex = get_u(msg="starting vertex for the DFS")
                           print("\n👉🏻 ", end="")
                           adj_list.dfs(start_vertex)
                           break    
                       # Invalid
                       case _:
                           print("\n❌ Invalid code number!")
                           continue

            
            # Displaying
            case "7":
                print("\n👇🏻 Here's your Adjacency List:")
                adj_list.display()
                
                
            # New Graph
            case "8":
                utility.clear()
                graph_intro("full")
                graph_main()
                break
            
            
            # New Data Structure
            case "9":
                utility.clear()
                utility.main_intro()
                break
            
            
            # Exiting the Program
            case "10":
                exit()
            
            
            # Invalid
            case _:
                print("\n🚫 Invalid operation code!")



# 🟥 =====> The Graph main & intro functions <=====

# 🎯 The Graph main function
## Since we have two different representations of a graph in the program, this main function just does pattern matching to their mains before breaking to transfer the control to the paramount main.py loop (after we break out of the other mains).
def graph_main():
    # Summoning the intro
    graph_intro("full")
        
    # 🟢 Graph Representation Type Selection loop
    while True:
        graph_repr = input("""\n🧪 Which type of graph representation do you want?
★1) Adjacency Matrix
★2) Adjacency List
>>> """)
    
        match graph_repr: 
            # Matrix
            case "1":
                adj_matrix_main()
                break
                
            # List 
            case "2":
                adj_list_main()
                break
             
            # Invalid
            case _:
                print("\n🚫 Invalid representation type code!")


# 🎁 The Graph intro function
def graph_intro(condition):
    graph_ascii = """\n
  .-_'''-.   .-------.       ____    .-------. .---.  .---.  
 '_( )_   \  |  _ _   \    .'  __ `. \  _(`)_ \|   |  |_ _|  
|(_ o _)|  ' | ( ' )  |   /   '  \  \| (_ o._)||   |  ( ' )  
. (_,_)/___| |(_ o _) /   |___|  /  ||  (_,_) /|   '-(_{;}_) 
|  |  .-----.| (_,_).' __    _.-`   ||   '-.-' |      (_,_)  
'  \  '-   .'|  |\ \  |  |.'   _    ||   |     | _ _--.   |  
 \  `-'`   | |  | \ `'   /|  _( )_  ||   |     |( ' ) |   |  
  \        / |  |  \    / \ (_ o _) //   )     (_{;}_)|   |  
   `'-...-'  ''-'   `'-'   '.(_,_).' `---'     '(_,_) '---'\n"""
    
    graph_def = """\n🎯 A graph is a non-linear data structure consisting of vertices (nodes) and edges that connect pairs of vertices. Graphs are used to model relationships between entities, making them essential in various fields such as computer science, biology, social networks, and transportation. Graphs can be directed or undirected, weighted or unweighted, and can contain cycles or be acyclic. The versatility of graphs allows them to represent complex structures and relationships, enabling efficient problem-solving and analysis. Graphs can be represented using either an Adjacency Matrix or an Adjacency List.

🌟 An adjacency matrix is a 2D array used to represent a graph, where the rows and columns correspond to vertices. The element at row (i) and column (j) indicates the presence and weight of an edge between vertices (i) and (j). For an undirected graph, the matrix is symmetric, while for a directed graph, it is not. The adjacency matrix allows for quick edge lookups with a time complexity of O(1), but it requires O(V^2) space, making it more suitable for dense graphs where the number of edges is close to the maximum possible.

🌟 An adjacency list represents a graph using an array of lists. Each element in the array corresponds to a vertex, and the list at each index contains the vertices adjacent to that vertex. This representation is more space-efficient for sparse graphs, as it only stores existing edges, resulting in a space complexity of O(V + E). Adjacency lists allow for efficient traversal of the graph, making them ideal for algorithms like Depth-First Search (DFS) and Breadth-First Search (BFS). However, edge lookups can be slower compared to an adjacency matrix, with a time complexity proportional to the degree of the vertex."""

    if condition == "full":
        print(graph_ascii)
        print(graph_def)
    elif condition == "def":
        print(graph_def)


# 🎁 The helper functions for getting the first vertex, second vertex & weight 
    
# First vertex
    # The msg param is used to customize the prompt in different cases
def get_u(msg="first vertex"):
    while True:
        u = utility.input_verify("int", msg)
        if u is None:
            print(f"\n🚫 Vertices are identified by integers in accordance with the matrix.")
            continue
        else:
            return u

# Second vertex
def get_v():
    while True:
        v = utility.input_verify("int", "second vertex")
        if v is None:
            print(f"\n🚫 Vertices are identified by integers in accordance with the matrix.")
            continue
        else:
            return v

# Weight
def get_weight():
    while True:
        weight = utility.input_verify("int", "weight")
        if weight is None:
            print(f"\n🚫 Weight can only be an INT.")
            continue
        else:
            return weight


# 🎯 Calling the Graph main function
if __name__ == "__main__":
    graph_main()
