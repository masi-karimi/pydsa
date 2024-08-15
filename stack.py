# Stack Implementation (static, dynamic-typed)

import utility


# 🎯 The Stack class
class Stack:
    
    def __init__(self, size):
        """
        Initializes a stack
        """
        self.size = size
        self.stack = []
        self.top = -1

    def is_empty(self):
        """
        Returns True if the stack is empty or false otherwise
        """
        return self.top == -1

    def is_full(self):
        """
        Returns True if the stack is full or false otherwise
        """
        return self.top == self.size - 1

    def push(self, item):
        """
        Pushes (inserts) an element into the stack the end of the stack
        """
        if not self.is_full():
            self.stack.append(item)
            self.top += 1
        else:
            print("\n🚫 Stack is full; item not pushed.", end="")

    def pop(self):
        """
        Pops (removes) & returns the element from the end of the stack
        """
        if not self.is_empty():
            item = self.stack.pop()
            self.top -= 1
            print(f"\n👋 Item removed: {item}", end="")
        else:
            print("\n🚫 Stack is empty.", end="")

    def peek(self):
        """
        Returns the element at the top of the stack
        """
        if not self.is_empty():
            top = self.stack[self.top]
            print(f"\n👉 Top item: {top}")
        else:
            print("\n🚫 Stack is empty.")
    
    def size_check(self):
        """
        Returns the size of the stack
        """
        print(f"\n👉 Stack size: {len(self.stack)}/{self.size}")
       
    def display(self):
        """
        Displays the stack
        """
        print(f"\n👉 {self.stack}")



# 🎯 The Stack main function
def stack_main():
    # Intro
    stack_intro("full")
    
    
    while True:
        example = input("""\n🛠️ Do you want to create a stack yourself or use the preloaded example?
●1) Create a stack
●2) Use the example
>>> """)
        match example:
            
            # Create a stack
            case "1":           
                # Stack size validation loop
                while True:
                    try:
                        stack_size = int(input("\n↔️ Please specify the size of the stack.\n>>> "))
                    except ValueError:
                        print("\n🚫 Invalid, the size can only be an integer!️")
                        continue
                    else:
                        break
                
                # Initializing & displaying the stack
                stack = Stack(stack_size)
                print("\n✅ Here's your stack:", end="")
                stack.display()
                break
            
            # Use the example
            case "2":
                stack = Stack(5)
                print("\n✅ Here's an example stack with size 5:", end="")
                stack.push(10)
                stack.push("Messi")
                stack.display()
                break
            
            # Invalid
            case _:
                print("\n❌ Invalid code number!")
                continue
                
    
    
    # 🟢 Operation selection loop
    while True:
        
        opr = input("""\n⚔️ Which operation do you want to perform with the STACK?
★0) Definition
★1) Pushing
★2) Popping
★3) Top/Peek
★4) isEmpty
★5) isFull
★6) Size Check
★7) Displaying
★8) New Stack
★9) New Data Structure
★10) Exit the Program

>>> """)

        match opr:
            
            # Definition
            case "0":
                stack_intro("def")
                
            # Pushing
            case "1":
                item = input("\n✍️ Please write the item.\n>>> ")
                
                try:
                    item = int(item)
                except ValueError:
                    pass
                else:
                    type = input("\n🤔 Do you want to add the item as an int or str? Type 1 for int or anything else for str.\n>>> ")
                    if type == "1":
                        pass
                    else:
                        item = str(item)
                stack.push(item)
                stack.display()


            # Popping
            case "2":
                stack.pop()
                stack.display()
            
            
            # Top/Peek
            case "3":
                stack.peek()
            
            
            # isEmpty
            case "4":
                result = stack.is_empty()
                print(f"\n👉 isEmpty: {result}")
            
            
            # isFull
            case "5":
                result = stack.is_full()
                print(f"\n👉 isFull: {result}")
                
            
            # Size Check
            case "6":
                stack.size_check()
            
            
            # Displaying
            case "7":
                stack.display()
            
            
            # New Stack
            case "8":
                utility.clear()
                utility.main_intro()
                stack_main()
                break
            
            
            # New Data Structure
            case "9":
                utility.clear()
                utility.main_intro()
                break
                
                
            # Exit the Program
            case "10":
                exit()
            
            
            # Invalid
            case _:
                print("\n🚫 Invalid operation code!")


# 🎁 Stack intro function
def stack_intro(condition):
    stack_ascii = """\n
   .-'''-. ,---------.    ____        _______   .--.   .--.   
  / _     \\          \ .'  __ `.    /   __  \  |  | _/  /    
 (`' )/`--' `--.  ,---'/   '  \  \  | ,_/  \__) | (`' ) /     
(_ o _).       |   \   |___|  /  |,-./  )       |(_ ()_)      
 (_,_). '.     :_ _:      _.-`   |\  '_ '`)     | (_,_)   __  
.---.  \  :    (_I_)   .'   _    | > (_)  )  __ |  |\ \  |  | 
\    `-'  |   (_(=)_)  |  _( )_  |(  .  .-'_/  )|  | \ `'   / 
 \       /     (_I_)   \ (_ o _) / `-'`-'     / |  |  \    /  
  `-...-'      '---'    '.(_,_).'    `._____.'  `--'   `'-'\n"""
    
    stack_def = "\n🎯 A stack is a linear data structure that operates on the Last In, First Out (LIFO) principle, akin to a stack of plates where the last plate placed on top is the first one to be removed. It supports two primary operations: push, which adds an element to the top of the stack, and pop, which removes the most recently added element from the top. Additionally, stacks often provide a peek operation to view the top element without removing it, and utility functions to check if the stack is empty or full. This structure is widely used in computer science for tasks such as managing function calls, undo mechanisms in applications, and algorithmic problems like parsing expressions. This program implements a dynamic-typed, fixed-size stack."
    
    if condition == "full":
        print(stack_ascii)
        print(stack_def)
    elif condition == "def":
        print(stack_def)


# 🎯 Calling the Stack main function
if __name__ == "__main__":
    stack_main()
