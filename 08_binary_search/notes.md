# 08 Binary Search - Code Breakdown

1. **Imports and Function Definitions:**
   ```python
   import random
   import time
   ```
   The code starts by importing two standard Python libraries: `random` for generating random numbers and `time` for measuring time intervals.

   Then, two functions are defined:
   - `naive_search(l, target)`: This function performs a naive search through the list `l` to find the `target` value. It returns the index of the target if found, otherwise -1.
   - `binary_search(l, target, low=None, high=None)`: This function implements the binary search algorithm to find the `target` value in the sorted list `l`. It returns the index of the target if found, otherwise -1.

2. **Main Code Execution:**
   ```python
   if __name__=='__main__':
   ```
   This conditional block ensures that the following code is executed only if the script is run directly, not if it's imported as a module in another script.

3. **List Initialization and Target Definition:**
   ```python
       l = [1, 3, 5, 10, 12]
       target = 10
   ```
   Two variables are initialized: `l` represents a sorted list, and `target` is the value we want to search for in the list.

4. **Function Calls and Output Printing:**
   ```python
       print(naive_search(l, target)) # 3
       print(binary_search(l, target)) # 3
   ```
   Here, both the `naive_search` and `binary_search` functions are called with the `l` list and `target` value as arguments. The results of these function calls are printed, showing the index of the target value in the list.

5. **Performance Comparison:**
   ```python
       length = 10000
       sorted_list = set()
       while len(sorted_list) < length:
           sorted_list.add(random.randint(-3*length, 3*length))
       sorted_list = sorted(list(sorted_list))
   ```
   This section generates a sorted list (`sorted_list`) of random integers within a specified range. The length of this list is set to 10000.

6. **Time Measurement:**
   ```python
       start = time.time()
       for target in sorted_list:
           naive_search(sorted_list, target)
       end = time.time()
       print("Naive search time: ", (end - start)/length, "seconds")
   ```
   This part measures the time taken by the `naive_search` function to search for each element in the `sorted_list`. The average search time per element is calculated and printed.

   Similarly, the time taken by the `binary_search` function is measured in the next section.

7. **Output Printing:**
   ```python
       start = time.time()
       for target in sorted_list:
           binary_search(sorted_list, target)
       end = time.time()
       print("Binary search time: ", (end - start)/length, "seconds")
   ```
   This section measures the time taken by the `binary_search` function to search for each element in the `sorted_list`. The average search time per element is calculated and printed.

That's the step-by-step breakdown of the provided Python code. It demonstrates the difference in performance between naive search and binary search algorithms for finding elements in a sorted list.