# Linked List Implementation (Singly & Doubly)

import utility


# 🟥 ===> Singly Linked List <===

# 🎯 The SLL Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# 🎯 The Singly Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # 🖐🏻 Using fingers as nodes for visualizing the different scenarios & index handlings can help big time!
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print("\n✅ Insertion successful.", end="")
        self.traverse()


    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print("\n✅ Insertion successful.", end="")
            self.traverse()
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        print("\n✅ Insertion successful.", end="")
        self.traverse()


    def insert_at_position(self, position, data):
        # = Insert to the Beginning
        if position == 0:
            self.insert_at_beginning(data)
            return
        # Normal
        new_node = Node(data)
        current = self.head
        ## Adding to the next index not being a problem, catching a None if the index leaves at least two positions empty 
        for _ in range(position - 1):
            if current is None:
                print("\n🚫 Position out of bounds. Insertion unsuccessful.")
                return
            current = current.next
        ## Catching a None if the index leaves only one position empty in between
        if current is None:
                print("\n🚫 Position out of bounds. Insertion unsuccessful.")
                return
        new_node.next = current.next
        current.next = new_node
        print("\n✅ Insertion successful.", end="")
        self.traverse()


    def delete_from_beginning(self):
        if self.head is None:
            print("\n🚫 List is empty.")
        # We may either return in the if block to exit the funcion or use else — more readable IMHO.
        else:
            self.head = self.head.next
            print("\n✅ Deletion successful.", end="")
            self.traverse()


    def delete_from_end(self):
        # Empty list
        if self.head is None:
            print("\n🚫 List is empty.")
            return
        # Just the head available
        if self.head.next is None:
            self.head = None
            print("\n✅ Deletion successful.", end="")
            self.traverse()
            return
        # Normal
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None
        print("\n✅ Deletion successful.", end="")
        self.traverse()
        
    
    def delete_from_position(self, position):
        # Empty list
        if self.head is None:
            print("\n🚫 List is empty.")
            return
        # Just having the head
        if position == 0:
            self.head = self.head.next
            print("\n✅ Deletion successful.", end="")
            self.traverse()
            return
        # Normal
        current = self.head
        ## Catching a None if it's at least two positions away from the last item
        for _ in range(position - 1):
            if current.next is None:
                print("\n🚫 Position out of bounds. Deletion unsuccessful.")
                return
            current = current.next
        ## Catching a None if it's only one position away from the last item (directly after the last)
        if current.next is None:
            print("\n🚫 Position out of bounds. Deletion unsuccessful.")
            return
        current.next = current.next.next
        print("\n✅ Deletion successful.", end="")
        self.traverse()


    def traverse(self):
        current = self.head
        if current is None:
            print("\n❌ List is empty.")
            return
        # The list for holding the elements to later print them with an arrow in between. Never Declare inside a loop since it'll be reset in every iteration, totally defying the purpose!
        # Since sep.join(list) method expects each list item to be a string, we typecast before appending. Using this method is preferred over a for loop since the loop would end up printing the arrow after the last item, too.
        sll_items = []
        while current:
            sll_items.append(str(current.data))
            current = current.next
        print("\n👉", " => ".join(sll_items))


    # Linear search, the only one suitable for linked lists
    def search(self, target):
        current = self.head
        position = 0
        while current:
            if current.data == target:
                print(f"\n✅ Item found at position {position}.")
                return position
            current = current.next
            position += 1
        print("\n❌ Item not found.")
        return -1


# 🎯 The Singly Linked List main function
def sll_main():
    
    # Creating an SLL object to gain access to the methods of its related class
    sll = SinglyLinkedList()
    
    # 🟢 Operation selection loop
    while True:

        opr = input("""\n⚔️ Which operation do you want to perform with the SINGLY LINKED LIST?
★0) Definition
★1) Insertion at the Beginning
★2) Insertion at a Specific Point
★3) Insertion at the End
★4) Deletion from the Beginning
★5) Deletion from a Specific Point
★6) Deletion from the End
★7) Traversing/Displaing
★8) Searching
★9) New Linked List
★10) New Data Structure
★11) Exiting the Program

>>> """)

        match opr:
            
            # Definition
            case "0":
                ll_intro("def")
            
            
            # Insertion at the Beginning 
            case "1":
                item = utility.input_verify()
                if item != None:
                    sll.insert_at_beginning(item)
                else:
                    print("\n🚫 Invalid data type; item not inserted.")


            # Insertion at a Specific Point 
            case "2":
                ## Index verification loop
                while True:
                    index = input("\n🔟 Please enter the index.\n>>> ")
                    try:
                        index = int(index)
                    except ValueError:
                        print("\n🚫 Invalid index!")
                        continue
                    else:
                        break
 
                item = utility.input_verify()
                if item != None:
                    sll.insert_at_position(index, item)
                else:
                    print("\n🚫 Invalid data type; item not inserted.")            
            
            
            # Insertion at the End
            case "3":
                item = utility.input_verify()
                if item != None:
                    sll.insert_at_end(item)
                else:
                    print("\n🚫 Invalid data type; item not inserted.")
            
            
            # Deletion from the Beginning
            case "4":
                sll.delete_from_beginning()
            
            
            # Deletion from a Specific Point
            case "5":
                ## Index verification loop
                while True:
                    index = input("\n🔟 Please enter the index.\n>>> ")
                    try:
                        index = int(index)
                    except ValueError:
                        print("\n🚫 Invalid index!")
                        continue
                    else:
                        break
                
                sll.delete_from_position(index)
            
            
            # Deletion from the End
            case "6":
                sll.delete_from_end()
            
            
            # Traversing
            case "7":
                sll.traverse()
            
            
            # Searching
            case "8":
                print("\nℹ️ Linear Search in the context of a linked list involves traversing the list node by node, starting from the head, and comparing each node’s data with the target value until the desired element is found or the end of the list is reached. Since linked lists do not provide direct access to their elements, each node must be accessed sequentially, making the search process inherently linear. The time complexity of linear search in a linked list is O(n), where n is the number of nodes in the list, because in the worst case, every node must be checked. The space complexity is O(1) as it requires no additional memory beyond the input list. Linear search is simple to implement and works well for small or unsorted linked lists, but it is inefficient for large lists compared to more advanced search algorithms.")
                target = input("\n🤔 Please provide the target element.\n>>> ")
                sll.search(target)
            
            
            # New Linked List
            case "9":
                utility.clear()
                utility.main_intro()
                linked_list_main()
                break
            
            
            # New Data Structure
            case "10":
                utility.clear()
                utility.main_intro()
                break
            
            
            # Exiting the Program
            case "11":
                exit()
            
            
            # Invalid
            case _:
                print("\n🚫 Invalid operation code!")



# 🟥 ===> Doubly Linked List <===

# 🎯 The DLL Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# 🎯 The Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None


    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
        print("\n✅ Insertion successful.", end="")
        self.traverse_forward()

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print("\n✅ Insertion successful.", end="")
            self.traverse_forward()
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last
        print("\n✅ Insertion successful.", end="")
        self.traverse_forward()

    def insert_at_position(self, position, data):
        if position == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        # Catching all None cases except the one right after the final item
        for _ in range(position):
            if current is None:
                print("\n🚫 Position out of bounds. Insertion unsuccessful.")
                return
            current = current.next
        # Catching the None right after the final item & passing control to insert_at_end()
        if current is None:
                self.insert_at_end(data)
                return
        new_node.prev = current.prev
        new_node.next = current
        current.prev.next = new_node
        current.prev = new_node
        print("\n✅ Insertion successful.", end="")
        self.traverse_forward()


    def delete_from_beginning(self):
        if self.head is None:
            print("\n🚫 List is empty.")
            return
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        print("\n✅ Deletion successful.", end="")
        self.traverse_forward()

    def delete_from_end(self):
        if self.head is None:
            print("\n🚫 List is empty.")
            return
        if self.head.next is None:
            self.head = None
            print("\n✅ Deletion successful.", end="")
            self.traverse_forward()
            return
        last = self.head
        while last.next:
            last = last.next
        last.prev.next = None
        print("\n✅ Deletion successful.", end="")
        self.traverse_forward()
        

    def delete_from_position(self, position):
        if self.head is None:
            print("\n🚫 List is empty.")
            return
        current = self.head
        for _ in range(position):
            current = current.next
            if current is None:
                print("\n🚫 Position out of bounds. Deletion unsuccessful.")
                return
        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next
        print("\n✅ Deletion successful.", end="")
        self.traverse_forward()


    def traverse_forward(self):
        current = self.head
        if current is None:
            print("\n👉 List is empty.")
        else: # if-else
            dll_items = []
            while current:
                dll_items.append(str(current.data))
                current = current.next
            print("\n👉", " <=> ".join(dll_items))

    def traverse_backward(self):
        current = self.head
        if current is None:
            print("\n👉 List is empty.")
            return # alt way
        while current.next:
            current = current.next
        dll_items=[]
        while current:
            dll_items.append(str(current.data))
            current = current.prev
        print("\n👉", " <=> ".join(dll_items))
    
    
    # Linear search, only suitable algorithm for linked lists
    def search(self, target):
        current = self.head
        position = 0
        while current:
            if current.data == target:
                print(f"\n✅ Item found at position {position}.")
                return position
            current = current.next
            position += 1
        print("\n❌ Item not found.")
        return -1


# 🎯 The Doubly Linked List main function
def dll_main():
    
    # Creating a DLL object to gain access to the methods of its related class
    dll = DoublyLinkedList()
    
    # 🟢 Operation selection loop
    while True:

        opr = input("""\n⚔️ Which operation do you want to perform with the DOUBLY LINKED LIST?
★0) Definition
★1) Insertion at the Beginning
★2) Insertion at a Specific Point
★3) Insertion at the End
★4) Deletion from the Beginning
★5) Deletion from a Specific Point
★6) Deletion from the End
★7) Traversing Forward
★8) Traversing Backward
★9) Searching
★10) New Linked List
★11) New Data Structure
★12) Exiting the Program

>>> """)

        match opr:
            
            # Definition
            case "0":
                ll_intro("def")
             
             
            # Insertion at the Beginning 
            case "1":
                item = utility.input_verify()
                if item != None:
                    dll.insert_at_beginning(item)
                else:
                    print("\n🚫 Invalid data type; item not inserted.")


            # Insertion at a Specific Point 
            case "2":
                ## Index verification loop
                while True:
                    index = input("\n🔟 Please enter the index.\n>>> ")
                    try:
                        index = int(index)
                    except ValueError:
                        print("\n🚫 Invalid index!")
                        continue
                    else:
                        break
 
                item = utility.input_verify()
                if item != None:
                    dll.insert_at_position(index, item)
                else:
                    print("\n🚫 Invalid data type; item not inserted.")            
            
            
            # Insertion at the End
            case "3":
                item = utility.input_verify()
                if item != None:
                    dll.insert_at_end(item)
                else:
                    print("\n🚫 Invalid data type; item not inserted.")
            
            
            # Deletion from the Beginning
            case "4":
                dll.delete_from_beginning()
            
            
            # Deletion from a Specific Point
            case "5":
                ## Index verification loop
                while True:
                    index = input("\n🔟 Please enter the index.\n>>> ")
                    try:
                        index = int(index)
                    except ValueError:
                        print("\n🚫 Invalid index!")
                        continue
                    else:
                        break
                
                dll.delete_from_position(index)
            
            
            # Deletion from the End
            case "6":
                dll.delete_from_end()
            
            
            # Traversing Forward
            case "7":
                dll.traverse_forward()
            
            
            # Traversing Backward
            case "8":
                dll.traverse_backward()
            
            
            # Searching
            case "9":
                target = input("\n🤔 Please provide the target element.\n>>> ")
                dll.search(target)
            
            
            # New Linked List
            case "10":
                utility.clear()
                utility.main_intro()
                linked_list_main()
                break
            
            
            # New Data Structure
            case "11":
                utility.clear()
                utility.main_intro()
                break
            
            
            # Exiting the Program
            case "12":
                exit()
            
            
            # Invalid
            case _:
                print("\n🚫 Invalid operation code!")



# 🪙 ===> The Linked List main & intro functions <===

# 🎯 The Linked List main function
## Since we have two types of linked lists in the program, this main function just does pattern matching to their mains before breaking to transfer the control to the paramount main.py loop (after we break out of the other mains).
def linked_list_main():
    # Summoning the intro
    ll_intro("full")
        
    # 🟢 Linked List Type Selection loop
    while True:
        list_type = input("""\n🧪 Which type of linked list do you want?
★1) Singly Linked List
★2) Doubly Linked List
    
>>> """)
    
        match list_type: 
            # Singly
            case "1":
                sll_main()
                break
                
            # Doubly 
            case "2":
                dll_main()
                break
             
            # Invalid
            case _:
                print("\n🚫 Invalid!")


# 🎁 The Linked List intro function
def ll_intro(condition):
    ll_ascii = """\n
  .---.    .-./`) ,---.   .--..--.   .--.      .-''-.   ______               .---.    .-./`)    .-'''-. ,---------.  
  | ,_|    \ .-.')|    \  |  ||  | _/  /     .'_ _   \ |    _ `''.           | ,_|    \ .-.')  / _     \\          \ 
,-./  )    / `-' \|  ,  \ |  || (`' ) /     / ( ` )   '| _ | ) _  \        ,-./  )    / `-' \ (`' )/`--' `--.  ,---' 
\  '_ '`)   `-'`"`|  |\_ \|  ||(_ ()_)     . (_ o _)  ||( ''_'  ) |        \  '_ '`)   `-'`"`(_ o _).       |   \    
 > (_)  )   .---. |  _( )_\  || (_,_)   __ |  (_,_)___|| . (_) `. |         > (_)  )   .---.  (_,_). '.     :_ _:    
(  .  .-'   |   | | (_ o _)  ||  |\ \  |  |'  \   .---.|(_    ._) '        (  .  .-'   |   | .---.  \  :    (_I_)    
 `-'`-'|___ |   | |  (_,_)\  ||  | \ `'   / \  `-'    /|  (_.\.' /          `-'`-'|___ |   | \    `-'  |   (_(=)_)   
  |        \|   | |  |    |  ||  |  \    /   \       / |       .'            |        \|   |  \       /     (_I_)    
  `--------`'---' '--'    '--'`--'   `'-'     `'-..-'  '-----'`              `--------`'---'   `-...-'      '---'\n"""
    
    ll_def = """\n🎯 A linked list is a dynamic data structure used to store a collection of elements, called nodes, in a sequential manner. Each node in a linked list contains data and a reference (or link) to the next node, forming a chain. Unlike arrays, linked lists do not require contiguous memory allocation, which allows for efficient insertion and deletion of nodes as there is no need to shift elements. This flexibility makes linked lists suitable for applications where the data size varies dynamically and frequent modifications are required.

🌟 Linked lists come in several types, each serving different purposes:

🔹 Singly Linked List: Each node has a single link to the next node, allowing one-way traversal.
🔹 Doubly Linked List: Nodes have two links, one to the next node and one to the previous, enabling traversal in both directions.
🔹 Singly Circular Linked List: Similar to a singly linked list, but the last node links back to the first node, forming a loop for circular traversal.
🔹 Doubly Circular Linked List: An extension of the doubly linked list where the last node links to the first, and the first node links to the last, allowing circular traversal in both directions."""

    if condition == "full":
        print(ll_ascii)
        print(ll_def)
    elif condition == "def":
        print(ll_def)


# 🎯 Calling the Linked List main function
if __name__ == "__main__":
    linked_list_main()
