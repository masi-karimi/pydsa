# Array Implementation (static, fixed-type)
# Module is named my_array to avoid conflict with Python's built-in array module.

import utility


# 🎯 The Array class
class Array:
    def __init__(self, size, data_type, default_value=None):
        """
        Initializes an array with a size, data type & default value
        """
        self.size = size
        self.data_type = data_type
        self.default_value = default_value
        self.array = [default_value] * size if default_value is None or isinstance(default_value, data_type) else [data_type()] * size


    def insert(self, index, value):
        """
        Inserts an element into a specific index of the array
        """
        if not isinstance(value, self.data_type):
            print(f"\n🚫 TypeError(Array can only contain elements of type {self.data_type.__name__}; item not inserted.)")
        else:
            if 0 <= index < self.size:
                self.array[index] = value
            else:
                print("\n🚫 IndexError(Array index out of bounds; item not inserted.)")


    def remove(self, index):
        """
        Removes an element from a specific index of the array
        """
        if 0 <= index < self.size:
            self.array[index] = self.default_value
        else:
            print("\n🚫 IndexError(Array index out of bounds. Deletion unsuccessful.)")
    
            
    def get(self, index):
        """
        Returns an element from a specific index of the array
        """
        if 0 <= index < self.size:
            print(f"\n👉 {self.array[index]}")
        else:
            print("\n🚫 IndexError(Array index out of bounds.)")


    def display(self):
        """
        Displays the entire array
        """
        print(f"\n👉 {self.array}")
        
        # for i in range(self.size):
            # print(f"Index {i}: {self.array[i]}")
    
    
    # Python built-in sorting
    def sort(self):
        self.array = sorted(self.array)
        # self.array.sort() also possible since self.array is a list, so we can use list methods with it; however, writing self.sort() ends up referring to the Array class object with no sort method, thereby resulting in an error!
    
    
    def bubble_sort(self, order):
        """
        Sorts the array using the Bubble Sort algorithm
        """
        n = len(self.array)
        for i in range(n):
            for j in range(0, n-i-1):
                if (order == 'asc' and self.array[j] > self.array[j+1]) or (order == 'desc' and self.array[j] < self.array[j+1]):
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
                    print("🔹", self.array)
        return self.array # Not really needed here, all the sorting algorithms sort the array in place & calling the display is all we need to show the final, sorted array
    
    
    def selection_sort(self, order):
        """
        Sorts the array using the Selection Sort algorithm
        """
        # Get the length of the array
        n = len(self.array)

        # Traverse through all array elements
        for i in range(n):
            # Find the minimum element in remaining unsorted array
            min_max_index = i
            for j in range(i+1, n):
                if (order == 'asc' and self.array[min_max_index] > self.array[j]) or \
                   (order == 'desc' and self.array[min_max_index] < self.array[j]):
                    min_max_index = j            
            # Swap the found minimum/maximum element with the first element
            self.array[i], self.array[min_max_index] = self.array[min_max_index], self.array[i]
            print("🔹", self.array)

        return self.array

    
    def insertion_sort(self, order):
        """
        Sorts the array using the Insertion Sort algorithm
        """
        # Traverse from 1 to len(self.array)
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i-1
            # Move elements of self.array[0..i-1], that are
            # greater/smaller than key, to one position ahead
            # of their current position
            while j >= 0 and ((order == 'asc' and key < self.array[j]) or (order == 'desc' and key > self.array[j])):
                self.array[j+1] = self.array[j]
                j -= 1
            self.array[j+1] = key
            print("🔹", self.array)
        return self.array


    def quick_sort(self, order):
        """
        Helper Method for Quick Sort
        """
        def partition(arr, low, high, order):
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                if (order == 'asc' and arr[j] <= pivot) or (order == 'desc' and arr[j] >= pivot):
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            print("🔹", self.array)
            return i + 1

        def quicksort_recursive(arr, low, high, order):
            """
            Sorts the array using the Quick Sort algorithm
            """
            if low < high:
                pi = partition(arr, low, high, order)
                quicksort_recursive(arr, low, pi - 1, order)
                quicksort_recursive(arr, pi + 1, high, order)

        quicksort_recursive(self.array, 0, len(self.array) - 1, order)
        return self.array
        
    
    def heapify(self, n, i, order):
        """
        Helper method for Heap Sort
        """
        # Initialize largest as root
        largest_smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # See if left child of root exists and is greater than root
        if order == 'asc' and left < n and self.array[i] < self.array[left]:
            largest_smallest = left
        elif order == 'desc' and left < n and self.array[i] > self.array[left]:
            largest_smallest = left

        # See if right child of root exists and is greater than root
        if order == 'asc' and right < n and self.array[largest_smallest] < self.array[right]:
            largest_smallest = right
        elif order == 'desc' and right < n and self.array[largest_smallest] > self.array[right]:
            largest_smallest = right

        # Change root, if needed
        if largest_smallest != i:
            self.array[i], self.array[largest_smallest] = self.array[largest_smallest], self.array[i]  # swap
            # Heapify the root
            self.heapify(n, largest_smallest, order)

    def heap_sort(self, order):
        """
        Sorts the array using the Heap Sort algorithm
        """
        n = len(self.array)

        # Build a max/min heap
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i, order)
            print("🔹", self.array)

        # One by one extract elements
        for i in range(n-1, 0, -1):
            self.array[i], self.array[0] = self.array[0], self.array[i]  # swap
            print("🔹", self.array)
            
            self.heapify(i, 0, order)
            print("🔹", self.array)

        return self.array
    
    
    def shell_sort(self, order):
        """
        Sorts the array using the Shell Sort algorithm
        """
        n = len(self.array)
        gap = n // 2

        # Start with a big gap, then reduce the gap
        while gap > 0:
            # Do a gapped insertion sort for this gap size.
            # The first gap elements self.array[0..gap-1] are already in gapped order
            # keep adding one more element until the entire array is gap sorted
            for i in range(gap, n):
                temp = self.array[i]
                # Shift earlier gap-sorted elements up until the correct location
                # for self.array[i] is found
                j = i
                while j >= gap and ((order == 'asc' and self.array[j - gap] > temp) or (order == 'desc' and self.array[j - gap] < temp)):
                    self.array[j] = self.array[j - gap]
                    j -= gap

                # Put temp (the original self.array[i]) in its correct location
                self.array[j] = temp
            print("🔹", self.array)
            gap //= 2
            
        return self.array
 
               
    def sort_intro(self):
        """
        UI helper method
        """
        print("\n📌 Initial array:", end="")
        self.display()
        print("\n🪜 Sorting Steps:",)
        

    def sort_outro(self):
        """
        UI helper method
        """
        print("\n♻️ Sorted array:", end="")
        self.display()
    
    
    def linear_search(self, target):
        """
        Searches the array using the Linear Search algorithm
        """
        for index, value in enumerate(self.array):
            if value == target:
                print(f"\n✅ Element found at index: {index}.")
                return index
        print("\n❌ Element not found.")
        return -1
    
    
    def binary_search(self, target):
        """
        Searches the array using the Binary Search algorithm
        """
        index_mapping = {value: index for index, value in enumerate(self.array)}
        # Create a copy of the original array to sort
        sorted_array = self.array[:]
        # Sort the copy using Python's built-in sort method
        sorted_array.sort()

        left, right = 0, len(sorted_array) - 1
        while left <= right:
            mid = (left + right) // 2
            if sorted_array[mid] == target:
                # Use the index mapping to find the original index
                original_index = index_mapping[sorted_array[mid]]
                print(f"\n✅ Element found at index: {original_index}.")
                return  # Exit after printing the result
            elif sorted_array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        print("\n❌ Element not found.")
    
    
    def size_check(self):
        """
        Returns the size of the array
        """
        size = self.size
        print(f"\n👉 Array size: {size}")
    
    
    def type_check(self):
        """
        Returns the data type of the array
        """
        data_type = self.data_type.__name__
        print(f"\n👉 Array Data Type: {data_type}")



# 🎯 The Array main function
def array_main():
    # Intro
    array_intro("full")
    
    while True:
        example = input("""\n🛠️ Do you want to create an array yourself or use the preloaded example?
●1) Create an array
●2) Use the example
>>> """)
        match example:
            
            # Create an array
            case "1":
                # Array type validation loop
                while True:
                    array_type = input("\n🤔 Please specify the type of array. Write either str or int.\n>>> ")
                    if array_type not in ("str", "int"):
                        print("\n❌️ Either str or int!")
                        continue
                    break
                
                # Array size validation loop
                while True:
                    try:
                        array_size = int(input("\n↔️ Please specify the size of the array.\n>>> "))
                    except ValueError:
                        print("\n❌ Invalid, the size can only be an integer!️")
                        continue
                    else:
                        break
                
                # Initializing the array
                if array_type == "str":
                    array = Array(array_size, str)
                else:
                    array = Array(array_size, int, 0)
                
                print(f"\n✅️ Here's your {array_type} array.", end="")
                array.display()
                break
            
            # Use Example
            case "2":
                array_type = "int"
                array_size = 5
                array = Array(5, int, 0)
                array.array = [10, 1987, 672, 8, 2004]
                print(f"\n✅️ Here's an example int array with size 5.", end="")
                array.display()
                break
            
            # Invalid
            case _:
                print("\n❌ Invalid code number!")
                continue 


    # 🟢 Operation selection loop
    while True:
        opr = input("""\n⚔️ Which operation do you want to perform with the ARRAY?
★0) Definition
★1) Insertion
★2) Deletion
★3) Indexing
★4) Sorting
★5) Searching
★6) Size Check
★7) Type Check
★8) Displaying
★9) New Array
★10) New Data Structure
★11) Exit the Program

>>> """)

        if opr not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"):
            print("\n❌️ Invalid code number.")
            continue
        
        # Definition
        if opr == "0":
            array_intro("def")
        
        
        # Insertion
        elif opr == "1":
            
            choice = input("\n➕️ Type 1 for adding one item or anything else for filling up the entire array.\n>>> ")
            
            # Adding one item
            if choice == "1":
                item = input("\n✍️ Please write the item.\n>>> ")
                index = int(input("\n✍️ Please provide the index.\n>>> "))
            
                try:
                    if array_type == "int":
                        item = int(item)
                except ValueError:
                    pass
                
                array.insert(index, item)
                array.display()
            
            # Filling up the entire array    
            else:
                for i in range(array.size):
                    item = input(f"\n✍️ Please write the item for index {i}: ")
                    try:
                        if array_type == "int":
                            item = int(item)
                    except ValueError:
                        pass
                
                    array.insert(i, item)
                array.display()
        
        
        # Deletion  
        elif opr == "2":
            index = int(input("\n✍️ Please provide the index of the item you want to remove.\n>>> "))
            array.remove(index)
            array.display()
           
            
        # Indexing
        elif opr == "3":
            index = int(input("\n✍️ Please provide the index of the item you want to get.\n>>> "))
            array.get(index)
        
            
        # Sorting
        elif opr == "4":
            
            ## 🟢🟢 Sorting algorithm selection loop
            sort_alg = input("""\n🗂️ Which sorting algorithm do you want to use?
●1) Bubble sort
●2) Selection sort
●3) Insertion sort
●4) Quick sort
●5) Heap sort
●6) Shell sort
>>> """)
            match sort_alg:
                ## Bubble sort
                case "1":
                    sort_order = utility.order_verify()
                    print("\nℹ️ Bubble Sort is a straightforward comparison-based sorting algorithm that repeatedly traverses the list, comparing adjacent elements and swapping them if they are in the wrong order. This process continues until the list is sorted. The algorithm is named because smaller elements \"bubble\" to the top of the list while larger elements sink to the bottom with each pass. Despite its simplicity and ease of implementation, Bubble Sort is inefficient for large datasets due to its average and worst-case time complexity of O(n^2), where n is the number of items being sorted. Additionally, its best-case time complexity is O(n) when the list is already sorted, and it has a space complexity of O(1) since it only requires a constant amount of additional memory space. Bubble Sort is mainly used for educational purposes and small datasets where its simplicity is advantageous.")
                    if sort_order == "asc":
                        array.sort_intro()
                        array.bubble_sort("asc")
                    else:
                        array.sort_intro()
                        array.bubble_sort("desc")
                    array.sort_outro()
                
                ## Selection sort
                case "2":
                    sort_order = utility.order_verify()
                    print("\nℹ️ Selection Sort is a simple comparison-based sorting algorithm that divides the input list into two parts: a sorted sublist of items which is built up from left to right at the front of the list, and a sublist of the remaining unsorted items. The algorithm repeatedly selects the smallest (or largest, depending on the order) element from the unsorted sublist, swaps it with the leftmost unsorted element, and moves the sublist boundaries one element to the right. This process continues until the entire list is sorted. Selection Sort has an average and worst-case time complexity of O(n^2), where n is the number of items being sorted, and a best-case time complexity of O(n^2) as well, since it always performs the same number of comparisons regardless of the initial order of the elements. Its space complexity is O(1) because it only requires a constant amount of additional memory space. Selection Sort is not suitable for large datasets but is easy to understand and implement, making it useful for educational purposes.")
                    if sort_order == "asc":
                        array.sort_intro()
                        array.selection_sort("asc")
                    else:
                        array.sort_intro()
                        array.selection_sort("desc")
                    array.sort_outro()
                
                ## Insertion sort
                case "3":
                    sort_order = utility.order_verify()
                    print("\nℹ️ Insertion Sort is a straightforward comparison-based sorting algorithm that builds the final sorted array one item at a time. It works by dividing the array into a sorted and an unsorted part. Initially, the sorted part contains only the first element, and the unsorted part contains the rest. The algorithm repeatedly takes the first element from the unsorted part, compares it with the elements in the sorted part, and inserts it into its correct position. This process continues until all elements are sorted. Insertion Sort has an average and worst-case time complexity of O(n^2), where n is the number of items being sorted, and a best-case time complexity of O(n) when the array is already sorted. Its space complexity is O(1) because it requires only a constant amount of additional memory space. Insertion Sort is efficient for small datasets and nearly sorted arrays, making it useful for scenarios where simplicity and ease of implementation are important.")
                    if sort_order == "asc":
                        array.sort_intro()
                        array.insertion_sort("asc")
                    else:
                        array.sort_intro()
                        array.insertion_sort("desc")
                    array.sort_outro()
                
                ## Quick sort
                case "4":
                    sort_order = utility.order_verify()
                    print("\nℹ️ Quick Sort is an efficient, comparison-based sorting algorithm that uses the divide-and-conquer strategy to sort elements. It works by selecting a ‘pivot’ element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then recursively sorted. This process continues until the base case of an empty or single-element sub-array is reached, which is inherently sorted. Quick Sort has an average and best-case time complexity of O(n log n), making it faster than other O(n^2) algorithms like Bubble Sort and Selection Sort for large datasets. However, its worst-case time complexity is O(n^2), which occurs when the smallest or largest element is always chosen as the pivot. The space complexity of Quick Sort is O(log n) due to the stack space used by the recursive calls. Despite its worst-case scenario, Quick Sort is widely used because of its efficiency and performance in practice.")
                    if sort_order == "asc":
                        array.sort_intro()
                        array.quick_sort("asc")
                    else:
                        array.sort_intro()
                        array.quick_sort("desc")
                    array.sort_outro()
                
                ## Heap sort
                case "5":
                    sort_order = utility.order_verify()
                    print("\nℹ️ Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure to sort elements. It works by first building a max heap (or min heap for descending order) from the input array, which ensures that the largest (or smallest) element is at the root of the heap. The root element is then swapped with the last element of the heap, and the heap size is reduced by one. The heapify process is applied to the root to restore the heap property, and this process is repeated until the heap size is reduced to one. Heap Sort has an average, best-case, and worst-case time complexity of O(n log n), where n is the number of items being sorted, making it more efficient than O(n^2) algorithms like Bubble Sort and Selection Sort. Its space complexity is O(1) because it sorts the array in place without requiring additional memory. Heap Sort is particularly useful for large datasets where consistent performance is important.")
                    if sort_order == "asc":
                        array.sort_intro()
                        array.heap_sort("asc")
                    else:
                        array.sort_intro()
                        array.heap_sort("desc")
                    array.sort_outro()
                
                ## Shell sort
                case "6":
                    sort_order = utility.order_verify()
                    print("\nℹ️ Shell Sort is an in-place comparison-based sorting algorithm that generalizes insertion sort to allow the exchange of items that are far apart. The algorithm starts by sorting elements that are a certain gap distance apart, then progressively reduces the gap and performs a gapped insertion sort for each gap size. This process continues until the gap is reduced to one, at which point it becomes a standard insertion sort. The choice of gap sequence can significantly affect the performance of Shell Sort. Its average and worst-case time complexity can vary depending on the gap sequence used, but it generally ranges from O(n^1.5) to O(n^2). The best-case time complexity is O(n log n) when using an optimal gap sequence. Shell Sort has a space complexity of O(1) because it sorts the array in place without requiring additional memory. It is more efficient than simple quadratic algorithms like bubble sort and insertion sort, especially for medium-sized datasets.")
                    if sort_order == "asc":
                        array.sort_intro()
                        array.shell_sort("asc")
                    else:
                        array.sort_intro()
                        array.shell_sort("desc")
                    array.sort_outro()
                
                ## Invalid
                case _:
                    print("\n🚫 Invalid code number.")
        
                        
        # Searching
        elif opr == "5":
            
            ## 🟢🟢 Searching algorithm selection loop
            search_alg = input("""\n🔍 Which searching algorithm do you want to use?
●1) Linear search
●2) Binary search
>>> """)
            match search_alg:
                ## Linear search
                case "1":
                    print("\nℹ️ Linear Search is a straightforward search algorithm that checks each element in a list sequentially until the desired element is found or the list ends. It starts at the first element and compares each element with the target value. If a match is found, the search is successful, and the index of the element is returned. If the end of the list is reached without finding the target, the search concludes that the element is not present. Linear Search has a time complexity of O(n), where n is the number of elements in the list, because in the worst case, it may need to check every element. Its space complexity is O(1) since it requires no additional memory beyond the input list. Linear Search is simple to implement and works well for small or unsorted datasets, but it is inefficient for large lists compared to more advanced search algorithms like binary search.")
                    data_type = array.data_type.__name__
                    
                    if data_type == "int":
                        target = utility.input_verify("int", "target element")
                        if target is not None:
                            array.linear_search(target)
                        else:
                            print("\n🚫 Invalid data type!")
                            
                    elif data_type == "str":
                        target = utility.input_verify("str", "target element")
                        if target is not None:
                            array.linear_search(target)
                        else:
                            print("\n🚫 Invalid data type!")
                
                ## Binary search
                case "2":
                    print("\nℹ️ Binary Search is an efficient algorithm for finding an element in a sorted array by repeatedly dividing the search interval in half. It begins by comparing the target value to the middle element of the array. If the target value matches the middle element, the search is successful. If the target value is less than the middle element, the search continues on the left half of the array; otherwise, it continues on the right half. This process is repeated until the target value is found or the search interval is empty. Binary Search has a time complexity of O(log n), where n is the number of elements in the array, because it halves the search space with each step. Its space complexity is O(1) for the iterative version, as it requires a constant amount of additional memory. The best-case time complexity is O(1) when the target value is at the middle of the array.")
                    data_type = array.data_type.__name__
                    
                    if data_type == "int":
                        target = utility.input_verify("int", "target element")
                        if target is not None:
                            array.binary_search(target)
                        else:
                            print("\n🚫 Invalid data type!")
                            
                    elif data_type == "str":
                        target = utility.input_verify("str", "target element")
                        if target is not None:
                            array.binary_search(target)
                        else:
                            print("\n🚫 Invalid data type!")
                            
                ## Invalid
                case _:
                    print("\n🚫 Invalid code number!")
        
        
        # Size Check
        elif opr == "6":
            array.size_check()
            
        
        # Type Check
        elif opr == "7":
            array.type_check()
        
        
        # Displaying
        elif opr == "8":
            array.display()
        
        
        # New Array
        elif opr == "9":
            utility.clear()
            utility.main_intro()
            array_main()
            break
        
        
        # New Data Structure
        elif opr == "10":
            utility.clear()
            utility.main_intro()
            break
        
        
        # Exit the Program
        elif opr == "11":
            exit()
        


# 🎁 Array intro & other helper functions
def array_intro(condition):
    array_ascii = """\n
   ____    .-------.    .-------.       ____       ____     __  
 .'  __ `. |  _ _   \   |  _ _   \    .'  __ `.    \   \   /  / 
/   '  \  \| ( ' )  |   | ( ' )  |   /   '  \  \    \  _. /  '  
|___|  /  ||(_ o _) /   |(_ o _) /   |___|  /  |     _( )_ .'   
   _.-`   || (_,_).' __ | (_,_).' __    _.-`   | ___(_ o _)'    
.'   _    ||  |\ \  |  ||  |\ \  |  |.'   _    ||   |(_,_)'     
|  _( )_  ||  | \ `'   /|  | \ `'   /|  _( )_  ||   `-'  /      
\ (_ o _) /|  |  \    / |  |  \    / \ (_ o _) / \      /       
 '.(_,_).' ''-'   `'-'  ''-'   `'-'   '.(_,_).'   `-..-'\n"""
 
    array_def = "\n🎯 An array is a fundamental linear data structure in computer science, consisting of a collection of elements, each identified by at least one array index or key. These elements are of the same data type and are stored in contiguous memory locations, allowing for efficient access and manipulation of data. Arrays are characterized by their fixed size, which is defined at the time of creation, and the ability to directly access any element in constant time using its index. This makes arrays particularly useful for implementing algorithms that require quick retrieval and update operations, as well as for storing data that can be easily sorted and searched."
    
    if condition == "full":
        print(array_ascii)
        print(array_def)
    elif condition == "def":
        print(array_def)



# 🎯 Calling the Array main function
if __name__ == "__main__":
    array_main()
    