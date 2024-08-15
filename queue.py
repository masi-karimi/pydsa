# Queue Implementation (static, dynamic-typed)

import utility


# 🎯 The Queue class
class Queue:
      
    def __init__(self, size):
        """
        Initializes a queue
        """
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = -1
        self.length = 0

    def is_empty(self):
        """
        Returns True if the queue is empty or false otherwise
        """
        return self.length == 0

    def is_full(self):
        """
        Returns True if the queue is full or false otherwise
        """
        return self.length == self.size

    def size_check(self):
        """
        Returns the size of the queue
        """
        print(f"\n👉 Queue size: {self.length}/{self.size}")

    def enqueue(self, item):
        """
        Enqueues (inserts) an element to the front of the queue
        """
        if not self.is_full():
            self.rear = (self.rear + 1) % self.size  # wraparound
            self.queue[self.rear] = item
            self.length += 1
        else:
            print("\n🚫 Queue is full; item not enqueued.", end="")

    def dequeue(self):
        """
        Dequeues (removes) an element from the rear of the queue
        """
        if not self.is_empty():
            item = self.queue[self.front]
            # Striking out the dequeued item
            ## Typecasting to str is necessary since int object isn't iterable
            strikeout = ""
            item = str(item)
            for char in item:
                strikeout = strikeout + char + '\u0336'
            self.queue[self.front] = strikeout

            self.front = (self.front + 1) % self.size
            self.length -= 1
            return item
        else:
            print("\n🚫 Queue is empty.", end="")

    def get_front(self):
        """
        Returns the front of the queue
        """
        if not self.is_empty():
            front = self.queue[self.front]
            print(f"\n👉 Front item: {front}")
        else:
            print("\n🚫 Queue is empty.")

    def get_rear(self):
        """
        Returns the rear of the queue
        """
        if not self.is_empty():
            rear = self.queue[self.rear]
            print(f"\n👉 Rear item: {rear}")
        else:
            print("\n🚫 Queue is empty.")

    def display(self):
        """
        Displays the queue
        """
        print(f"\n👉 {self.queue}")



# 🎯 The Queue main function
def queue_main():
    # Intro
    queue_intro("full")
    
    while True:
        example = input("""\n🛠️ Do you want to create a queue yourself or use the preloaded example?
●1) Create a queue
●2) Use the example
>>> """)
        match example:
            
            # Create a queue
            case "1":          
                # Queue size validation loop
                while True:
                    try:
                        queue_size = int(input("\n↔️ Please specify the size of the queue.\n>>> "))
                    except ValueError:
                        print("\n❌ Invalid, the size can only be an integer!️")
                        continue
                    else:
                        break
            
                # Initializing & displaying the queue
                queue = Queue(queue_size)
                print("\n✅ Here's your queue:", end="")
                queue.display()
                break
            
            # Use the example
            case "2":
                queue = Queue(5)
                print("\n✅ Here's an example queue with size 5:", end="")
                queue.display()
                break
            
            # Invalid
            case _:
                print("\n❌ Invalid code number!")
                continue


    # 🟢 Operation selection loop
    while True:
        
        opr = input("""\n⚔️ Which operation do you want to perform with the QUEUE?
★0) Definition
★1) Enqueue
★2) Dequeue
★3) Front
★4) Rear
★5) isEmpty
★6) isFull
★7) Size Check
★8) Displaying
★9) New Queue
★10) New Data Structure
★11) Exit the Program

>>> """)

        match opr:
            
            # Definition
            case "0":
                queue_intro("def")
            
            # Enqueue
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
                queue.enqueue(item)
                queue.display()


            # Dequeue
            case "2":
                queue.dequeue()
                queue.display()
            
            
            # Front
            case "3":
                queue.get_front()
            
            
            # Rear
            case "4":
                queue.get_rear()
            
            
            # isEmpty
            case "5":
                result = queue.is_empty()
                print(f"\n👉 isEmpty: {result}.")
            
            
            # isFull
            case "6":
                result = queue.is_full()
                print(f"\n👉 isFull: {result}.")
            
            
            # Size Check
            case "7":
                queue.size_check()
            
            
            # Displaying
            case "8":
                queue.display()
            
            
            # New Queue
            case "9":
                utility.clear()
                utility.main_intro()
                queue_main()
                break
            
            
            # New Data Structure
            case "10":
                utility.clear()
                utility.main_intro()
                break
            
            
            # Exit the Program
            case "11":
                exit()
            
            
            # Invalid
            case _:
                print("\n🚫 Invalid operation code!")
                ## Auto continue with the While True in full swing!


# 🎁 Queue intro function
def queue_intro(condition):
    queue_ascii = """\n
    ,-----.      ___    _     .-''-.    ___    _     .-''-.   
  .'  .-,  '.  .'   |  | |  .'_ _   \ .'   |  | |  .'_ _   \  
 / ,-.|  \ _ \ |   .'  | | / ( ` )   '|   .'  | | / ( ` )   ' 
;  \  '_ /  | :.'  '_  | |. (_ o _)  |.'  '_  | |. (_ o _)  | 
|  _`,/ \ _/  |'   ( \.-.||  (_,_)___|'   ( \.-.||  (_,_)___| 
: (  '\_/ \   ;' (`. _` /|'  \   .---.' (`. _` /|'  \   .---. 
 \ `"/  \  )  \| (_ (_) _) \  `-'    /| (_ (_) _) \  `-'    / 
  '. \_/``"/)  )\ /  . \ /  \       /  \ /  . \ /  \       /  
    '-----' `-'  ``-'`-''    `'-..-'    ``-'`-''    `'-..-'\n"""
    
    queue_def = "\n🎯 A queue is a linear data structure that adheres to the First In, First Out (FIFO) principle, much like customers waiting in line where the first person in line is the first to be served. It supports two primary operations: enqueue, which adds an element to the end of the queue, and dequeue, which removes the element from the front. This structure is essential in various computing scenarios, such as task scheduling, data processing, and resource management, due to its ability to maintain order in processing tasks or data. Queues are implemented in software using arrays or linked lists and are integral in algorithms that require sequential data processing, ensuring that elements are handled in the exact order they were added. This program implements a dynamic-typed, fixed-size queue."
    
    if condition == "full":
        print(queue_ascii)
        print(queue_def)
    elif condition == "def":
        print(queue_def)


# 🎯 Calling the Queue main function
if __name__ == "__main__":
    queue_main()
