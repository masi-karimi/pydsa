import utility
import my_array
import stack
import queue
import linked_list
import tree
import graph
import hash_table


# 🌟🌟🌟 The main function
def main():

    # 🟢 The main & paramount selection loop (Linear vs Non-linear)! Breaking out of individual data structures with the New Data Structure operation returns control to here.
    while True:
        
        choice_1 = input("""\n📂 Which type of data structure do you want to learn?
★1) Linear data structures
★2) Non-linear data structures

>>> """)
        
        match choice_1:
            
            # 🟢 The Linear DSes section & selection loop
            case "1":
                while True:
                    choice_2 = input("""\n🏁 Which Linear Data Structure do you want to learn?
★1) Array
★2) Stack
★3) Queue
★4) Linked List

★0) Go Back

>>> """)
                    match choice_2:
                    
                        # Array
                        case "1":
                            my_array.array_main()
                            break
                        
                        # Stack
                        case "2":
                            stack.stack_main()
                            break
                        
                        # Queue
                        case "3":
                            queue.queue_main()
                            break
                        
                        # Linked List
                        case "4":
                            linked_list.linked_list_main()
                            break
                        
                        # Go Back
                        case "0":
                            main()
                            break
                            
                        # Invalid
                        case _:
                            print("\n❌ Invalid code number!️")
                            continue
           
    
            # 🟢 The Non-linear DSes section & selection loop
            case "2":
                while True:
                    choice_2 = input("""\n Which Non-linear Data Structure do you want to learn?
★1) Tree
★2) Graph
★3) Hash Table

★0) Go Back

>>> """)
                    match choice_2:
                    
                        # Tree
                        case "1":
                            tree.tree_main()
                            break
                        
                        # Graph
                        case "2":
                            graph.graph_main()
                            break
                        
                        # Hash Table
                        case "3":
                            hash_table.hash_table_main()
                            break
                        
                        # Go Back
                        case "0":
                           main()
                           break
                           
                        # Invalid selection   
                        case _:
                            print("\n❌ Invalid code number!️")
                            continue
            
            case _:
                print("\n❌ Invalid code number!")



# 🌟 Calling the functions & initializing the program
utility.main_intro()
main()
