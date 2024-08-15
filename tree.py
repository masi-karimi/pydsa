# Tree Implementation (BST & AVL)

import utility


# 🟥 =====> BST (Binary Search Tree) <=====

# 🎯 The BST Node class
class Node:
    def __init__(self, key):
        self.key = key  # The value of the node
        self.left = None  # Pointer to the left child
        self.right = None  # Pointer to the right child


# 🎯 The BST class
class BinarySearchTree:
    def __init__(self, type):
        self.root = None  # Initialize the root of the BST as None
        self.data_type = type # To keep the BST a home for either numbers or strings

    def insert(self, key):
        """Insert a new key into the BST."""
        if self.root is None:
            self.root = Node(key)  # If the tree is empty, set the root to the new node
        else:
            self._insert(self.root, key)  # Otherwise, call the helper method to insert the key

    def _insert(self, node, key):
        """Helper method to insert a new key into the BST."""
        if key < node.key:
            if node.left is None:
                node.left = Node(key)  # Insert the new node as the left child
            else:
                self._insert(node.left, key)  # Recursively insert in the left subtree
        else:
            if node.right is None:
                node.right = Node(key)  # Insert the new node as the right child
            else:
                self._insert(node.right, key)  # Recursively insert in the right subtree

    def search(self, key):
        """Search for a key in the BST."""
        return self._search(self.root, key)

    def _search(self, node, key):
        """Helper method to search for a key in the BST."""
        if node is None or node.key == key:
            return node  # Return the node if found, or None if not found
        if key < node.key:
            return self._search(node.left, key)  # Recursively search in the left subtree
        else:
            return self._search(node.right, key)  # Recursively search in the right subtree

    def delete(self, key):
        """Delete a key from the BST."""
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        """Helper method to delete a key from the BST."""
        if node is None:
            return node  # If the node is not found, return None
        if key < node.key:
            node.left = self._delete(node.left, key)  # Recursively delete from the left subtree
        elif key > node.key:
            node.right = self._delete(node.right, key)  # Recursively delete from the right subtree
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Node with two children: Get the in-order successor (smallest in the right subtree)
            temp = self._min_value_node(node.right)
            node.key = temp.key  # Copy the in-order successor's content to this node
            node.right = self._delete(node.right, temp.key)  # Delete the in-order successor
        return node

    def _min_value_node(self, node):
        """Helper method to find the node with the minimum key value."""
        current = node
        while current.left is not None:
            current = current.left  # Move to the leftmost node
        return current

    def inorder(self):
        """Perform in-order traversal of the BST."""
        return self._inorder(self.root)

    def _inorder(self, node):
        """Helper method for in-order traversal."""
        res = []
        if node:
            res = self._inorder(node.left)  # Visit left subtree
            res.append(node.key)  # Visit node
            res = res + self._inorder(node.right)  # Visit right subtree
        return res

    def preorder(self):
        """Perform pre-order traversal of the BST."""
        return self._preorder(self.root)

    def _preorder(self, node):
        """Helper method for pre-order traversal."""
        res = []
        if node:
            res.append(node.key)  # Visit node
            res = res + self._preorder(node.left)  # Visit left subtree
            res = res + self._preorder(node.right)  # Visit right subtree
        return res

    def postorder(self):
        """Perform post-order traversal of the BST."""
        return self._postorder(self.root)

    def _postorder(self, node):
        """Helper method for post-order traversal."""
        res = []
        if node:
            res = self._postorder(node.left)  # Visit left subtree
            res = res + self._postorder(node.right)  # Visit right subtree
            res.append(node.key)  # Visit node
        return res


# 🎯 The BST main function
def bst_main():
    print("\nℹ️ This program implements a BST that allows nodes of the same general data type & allows duplicates on the right subtree of the root.")
    # 🟢 Starting loop (Going DIY or using the example)
    while True:
        example = input("""\n🛠️ Do you want to create a BST yourself or use the preloaded example?
●1) Create a BST
●2) Use the example
>>> """)
        match example:
            
            # Create a BST
            case "1":
                # 🟢 Type selection loop before creating a BST object to gain access to the methods of its related class
                while True:
                    type = input("""\n🤔 Which type of data do you want store in the BST?
★1) Numbers (int or float)
★2) Strings
>>> """)
                    match type:
                        case "1":
                            bst = BinarySearchTree("num")
                            break
                        case "2":
                            bst = BinarySearchTree("str")
                            break
                        case _:
                            print("Invalid code number!")
                            continue
                break      
                      
            # Use Example
            case "2":
                bst = BinarySearchTree("num")
                bst.insert(50)
                bst.insert(30)
                bst.insert(10)
                bst.insert(20)
                bst.insert(70)
                bst.insert(60)
                bst.insert(80)
                print("\n✅ Here's an example BST.", end="")
                print(f"\n👉🏻 {bst.inorder()}\nℹ️ Inorder Traversal")
                break
                
            # Invalid
            case _:
                print("\n❌ Invalid code number!")
                continue
    
    
    # 🟢 Operation selection loop
    while True:
        opr = input("""\n⚔️ Which operation do you want to perform with the BST?
★0) Definition
★1) Insertion
★2) Deletion
★3) Searching
★4) Traversals
★5) New Tree
★6) New Data Structure
★7) Exiting the Program

>>> """)
        match opr:
         
            # Definition
            case "0":
                tree_intro("def")
            
            
            # Insertion
            case "1":
                data_type = bst.data_type
                if data_type == "str":
                    item = utility.input_verify("str")
                elif data_type == "num":
                    item = utility.input_verify("num")
                
                if item != None:
                    bst.insert(item)
                    print("\n✅ Successfully inserted.", end="")
                    print(f"\n👉🏻 {bst.inorder()}\nℹ️ Inorder Traversal")
                else:
                    print("\n🚫 Invalid data type; item not inserted.")
            
            
            # Deletion
            case "2":
                data_type = bst.data_type
                if data_type == "str":
                    item = utility.input_verify("str")
                elif data_type == "num":
                    item = utility.input_verify("num")
                
                if item != None:
                    # When we get a valid input to consider for deleting
                    # Collecting all the nodes in the tree through inorder traversal to check if the input item is available in the tree & print node not found when negative.
                    nodes = bst.inorder()
                    if item not in nodes:
                        print("\n❌ Node not found. Deletion unsuccessful.")
                    else:
                        bst.delete(item)
                        print("\n✅ Successfully deleted.", end="")
                        print(f"\n👉🏻 {bst.inorder()}\nℹ️ Inorder Traversal")
                else:
                    print("\n🚫 Invalid data type. Deletion unsuccessful.")
                
                
            # Searching
            case "3":
                data_type = bst.data_type
                if data_type == "str":
                    item = utility.input_verify("str")
                elif data_type == "num":
                    item = utility.input_verify("num")
                    
                    if item != None:
                        result = bst.search(item)
                        if result != None:
                            print("\n✅ Node available.", end="")
                            print(f"\n👉🏻 {bst.inorder()}\nℹ️ Inorder Traversal")
                        else:
                            print("\n❌ Node not found.", end=" ")
                            print(f"\n👉🏻 {bst.inorder()}\nℹ️ Inorder Traversal")
                    else:
                        print("\n🚫 Invalid data type. Deletion unsuccessful.")
            
            
            # Traversals
            case "4":
               
               # Traversal type selection loop
               while True:
                   traversal_type = input("""\n🗂️ Which traversal do you want?
●1) Inorder Traversal
●2) Preorder Traversal
●3) Postorder Traversal
>>> """)
                   match traversal_type:
                
                       # Inorder
                       case "1":
                           print(f"\n👉🏻 {bst.inorder()}\nℹ️ Inorder Traversal")
                           break
                       
                       # Preorder
                       case "2":
                           print(f"\n👉🏻 {bst.preorder()}\nℹ️ Preorder Traversal")
                           break       
                        
                       # Postorder
                       case "3":
                           print(f"\n👉🏻 {bst.postorder()}\nℹ️ Postorder Traversal")
                           break
                        
                       # Invalid
                       case _:
                           print("\n❌ Invalid code number!")
                           continue


            # New Tree
            case "5":
                utility.clear()
                tree_intro("full")
                tree_main()
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



# 🟥 ==========> AVL Tree <==========

# 🎯 The AVL Node class
class Node:
    def __init__(self, key):
        self.key = key  # The value of the node
        self.left = None  # Pointer to the left child
        self.right = None  # Pointer to the right child
        self.height = 1  # Height of the node
        

# 🎯 The AVL class
class AVLTree:
    def __init__(self, type):
        self.root = None  # Initialize the root of the AVL tree as None
        self.data_type = type # To keep the AVL a home for either numbers or strings

    def insert(self, key):
        """Insert a new key into the AVL tree."""
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        """Helper method to insert a new key into the AVL tree."""
        if not node:
            return Node(key)  # Create a new node if the current node is None

        if key < node.key:
            node.left = self._insert(node.left, key)  # Insert in the left subtree
        else:
            node.right = self._insert(node.right, key)  # Insert in the right subtree

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))  # Update the height of the node

        balance = self._get_balance(node)  # Get the balance factor

        # Perform rotations to balance the tree
        if balance > 1 and key < node.left.key:
            return self._right_rotate(node)  # Left Left Case
        if balance < -1 and key > node.right.key:
            return self._left_rotate(node)  # Right Right Case
        if balance > 1 and key > node.left.key:
            node.left = self._left_rotate(node.left)  # Left Right Case
            return self._right_rotate(node)
        if balance < -1 and key < node.right.key:
            node.right = self._right_rotate(node.right)  # Right Left Case
            return self._left_rotate(node)

        return node

    def delete(self, key):
        """Delete a key from the AVL tree."""
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        """Helper method to delete a key from the AVL tree."""
        if not node:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)  # Delete from the left subtree
        elif key > node.key:
            node.right = self._delete(node.right, key)  # Delete from the right subtree
        else:
            if not node.left:
                return node.right  # Node with only right child or no child
            elif not node.right:
                return node.left  # Node with only left child

            temp = self._min_value_node(node.right)  # Node with two children
            node.key = temp.key  # Replace node's key with the in-order successor's key
            node.right = self._delete(node.right, temp.key)  # Delete the in-order successor

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))  # Update the height of the node

        balance = self._get_balance(node)  # Get the balance factor

        # Perform rotations to balance the tree
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotate(node)  # Left Left Case
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._left_rotate(node.left)  # Left Right Case
            return self._right_rotate(node)
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotate(node)  # Right Right Case
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)  # Right Left Case
            return self._left_rotate(node)

        return node

    def search(self, key):
        """Search for a key in the AVL tree."""
        return self._search(self.root, key)

    def _search(self, node, key):
        """Helper method to search for a key in the AVL tree."""
        if not node or node.key == key:
            return node  # Return the node if found, or None if not found

        if key < node.key:
            return self._search(node.left, key)  # Recursively search in the left subtree
        return self._search(node.right, key)  # Recursively search in the right subtree

    def inorder(self):
        """Perform in-order traversal of the AVL tree."""
        return self._inorder(self.root)

    def _inorder(self, node):
        """Helper method for in-order traversal."""
        res = []
        if node:
            res = self._inorder(node.left)  # Visit left subtree
            res.append(node.key)  # Visit node
            res = res + self._inorder(node.right)  # Visit right subtree
        return res

    def preorder(self):
        """Perform pre-order traversal of the AVL tree."""
        return self._preorder(self.root)

    def _preorder(self, node):
        """Helper method for pre-order traversal."""
        res = []
        if node:
            res.append(node.key)  # Visit node
            res = res + self._preorder(node.left)  # Visit left subtree
            res = res + self._preorder(node.right)  # Visit right subtree
        return res

    def postorder(self):
        """Perform post-order traversal of the AVL tree."""
        return self._postorder(self.root)

    def _postorder(self, node):
        """Helper method for post-order traversal."""
        res = []
        if node:
            res = self._postorder(node.left)  # Visit left subtree
            res = res + self._postorder(node.right)  # Visit right subtree
            res.append(node.key)  # Visit node
        return res

    def _left_rotate(self, z):
        """Perform a left rotation."""
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _right_rotate(self, z):
        """Perform a right rotation."""
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _get_height(self, node):
        """Get the height of the node."""
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        """Get the balance factor of the node."""
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _min_value_node(self, node):
        """Get the node with the minimum key value."""
        current = node
        while current.left is not None:
            current = current.left
        return current


# 🎯 The AVL main function
def avl_main():
    print("\nℹ️ This program implements an AVL that allows nodes of the same general data type & allows duplicates on the right subtree of the root.")
    # 🟢 Starting loop (Going DIY or using the example)
    while True:
        example = input("""\n🛠️ Do you want to create an AVL tree yourself or use the preloaded example?
●1) Create an AVL tree
●2) Use the example
>>> """)
        match example:
            
            # Create an AVL
            case "1":
                # 🟢 Type selection loop before creating an AVL object to gain access to the methods of its related class
                while True:
                    type = input("""\n🤔 Which type of data do you want store in the AVL?
★1) Numbers (int or float)
★2) Strings
>>> """)
                    match type:
                        case "1":
                            avl = AVLTree("num")
                            break
                        case "2":
                            bst = AVLTree("str")
                            break
                        case _:
                            print("Invalid code number!")
                            continue
                break      
                      
            # Use Example
            case "2":
                avl = AVLTree("num")
                avl.insert(50)
                avl.insert(30)
                avl.insert(10)
                avl.insert(20)
                avl.insert(70)
                avl.insert(60)
                avl.insert(80)
                print("\n✅ Here's an example AVL.", end="")
                print(f"\n👉🏻 {avl.inorder()}\nℹ️ Inorder Traversal")
                break
                
            # Invalid
            case _:
                print("\n❌ Invalid code number!")
                continue
    
    
    # 🟢 Operation selection loop
    while True:
        opr = input("""\n⚔️ Which operation do you want to perform with the AVL TREE?
★0) Definition
★1) Insertion
★2) Deletion
★3) Searching
★4) Traversals
★5) New Tree
★6) New Data Structure
★7) Exiting the Program

>>> """)
        match opr:
         
            # Definition
            case "0":
                tree_intro("def")
            
            
            # Insertion
            case "1":
                data_type = avl.data_type
                if data_type == "str":
                    item = utility.input_verify("str")
                elif data_type == "num":
                    item = utility.input_verify("num")
                
                if item != None:
                    avl.insert(item)
                    print("\n✅ Successfully inserted.", end="")
                    print(f"\n👉🏻 {avl.inorder()}\nℹ️ Inorder Traversal")
                else:
                    print("\n🚫 Invalid data type; item not inserted.")
            
            
            # Deletion
            case "2":
                data_type = avl.data_type
                if data_type == "str":
                    item = utility.input_verify("str")
                elif data_type == "num":
                    item = utility.input_verify("num")
                
                if item != None:
                    # When we get a valid input to consider for deleting
                    # Collecting all the nodes in the tree through inorder traversal to check if the input item is available in the tree & print node not found when negative.
                    nodes = avl.inorder()
                    if item not in nodes:
                        print("\n❌ Node not found. Deletion unsuccessful.")
                    else:
                        avl.delete(item)
                        print("\n✅ Successfully deleted.", end="")
                        print(f"\n👉🏻 {avl.inorder()}\nℹ️ Inorder Traversal")
                else:
                    print("\n🚫 Invalid data type. Deletion unsuccessful.")
                
                
            # Searching
            case "3":
                data_type = avl.data_type
                if data_type == "str":
                    item = utility.input_verify("str")
                elif data_type == "num":
                    item = utility.input_verify("num")
                    
                    if item != None:
                        result = avl.search(item)
                        if result != None:
                            print("\n✅ Node available.", end="")
                            print(f"\n👉🏻 {avl.inorder()}\nℹ️ Inorder Traversal")
                        else:
                            print("\n❌ Node not found.", end=" ")
                            print(f"\n👉🏻 {avl.inorder()}\nℹ️ Inorder Traversal")
                    else:
                        print("\n🚫 Invalid data type. Deletion unsuccessful.")
            
            
            # Traversals
            case "4":
               
               # Traversal type selection loop
               while True:
                   traversal_type = input("""\n🗂️ Which traversal do you want?
●1) Inorder Traversal
●2) Preorder Traversal
●3) Postorder Traversal
>>> """)
                   match traversal_type:
                
                       # Inorder
                       case "1":
                           print(f"\n👉🏻 {avl.inorder()}\nℹ️ Inorder Traversal")
                           break
                       
                       # Preorder
                       case "2":
                           print(f"\n👉🏻 {avl.preorder()}\nℹ️ Preorder Traversal")
                           break       
                        
                       # Postorder
                       case "3":
                           print(f"\n👉🏻 {avl.postorder()}\nℹ️ Postorder Traversal")
                           break
                        
                       # Invalid
                       case _:
                           print("\n❌ Invalid code number!")
                           continue


            # New Tree
            case "5":
                utility.clear()
                tree_intro("full")
                tree_main()
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



# 🟥 ===> The Tree main & intro functions <===

# 🎯 The Tree main function
## Since we have two types of trees in the program, this main function just does pattern matching to their mains before breaking to transfer the control to the paramount main.py loop (after we break out of the other mains).
def tree_main():
    # Summoning the intro
    tree_intro("full")
        
    # 🟢 Tree Type Selection loop
    while True:
        tree_type = input("""\n🧪 Which type of tree do you want?
★1) BST (Binary Search Tree)
★2) AVL (Adelson-Velsky and Evgenii Landis)  
>>> """)
    
        match tree_type: 
            # BST
            case "1":
                bst_main()
                break
                
            # AVL 
            case "2":
                avl_main()
                break
             
            # Invalid
            case _:
                print("\n🚫 Invalid type code!")


# 🎁 The Tree intro function
def tree_intro(condition):
    tree_ascii = """\n
,---------. .-------.        .-''-.      .-''-.   
\          \|  _ _   \     .'_ _   \   .'_ _   \  
 `--.  ,---'| ( ' )  |    / ( ` )   ' / ( ` )   ' 
    |   \   |(_ o _) /   . (_ o _)  |. (_ o _)  | 
    :_ _:   | (_,_).' __ |  (_,_)___||  (_,_)___| 
    (_I_)   |  |\ \  |  |'  \   .---.'  \   .---. 
   (_(=)_)  |  | \ `'   / \  `-'    / \  `-'    / 
    (_I_)   |  |  \    /   \       /   \       /  
    '---'   ''-'   `'-'     `'-..-'     `'-..-'\n"""
    
    tree_def = """\n🎯 A specialized type of graph, the tree is a hierarchical, non-linear data structure consisting of nodes connected by edges. It starts with a single node called the root, from which all other nodes branch out. Each node can have zero or more child nodes, and nodes with no children are called leaf nodes. Trees are used to represent hierarchical relationships and are fundamental in various applications such as file systems, databases, and network routing. They facilitate efficient data retrieval and manipulation through various traversal methods like in-order, pre-order, and post-order traversal.
🎯 Trees have many different types the most important of which is the Binary Tree which in which each node has at most 2 children. The binary tree can also be classified further down the line with the most popular ones being the BST & the AVL trees. PyDSA implements these two types of binary trees. 

🌟 A Binary Search Tree (BST) is a specialized type of binary tree where each node has at most two children, referred to as the left and right child. The key property of a BST is that for any given node, all values in its left subtree are less than the node's value, and all values in its right subtree are greater. This property allows for efficient searching, insertion, and deletion operations, typically with a time complexity of (O(log n)) if the tree is balanced. If not balanced, it's possible for the BST to develop a big difference between its left & right subtrees in which case the time complexity will degrade to (O(n)). That's why self-balancing BSTs like AVL & Red-Black tree are used. BSTs are widely used in applications that require dynamic data sets and quick lookups, such as databases and search engines.

🌟 An AVL tree is a self-balancing binary search tree named after its inventors, Georgy Adelson-Velsky and Evgenii Landis. In an AVL tree, the heights of the left and right subtrees of any node differ by at most one, ensuring the tree remains balanced. This balance is maintained through rotations during insertion and deletion operations. The AVL tree's balanced nature guarantees that operations such as search, insertion, and deletion have a time complexity of (O(log n)), making it highly efficient for applications requiring frequent data modifications and lookups."""

    if condition == "full":
        print(tree_ascii)
        print(tree_def)
    elif condition == "def":
        print(tree_def)


# 🎯 Calling the Tree main function
if __name__ == "__main__":
    tree_main()
