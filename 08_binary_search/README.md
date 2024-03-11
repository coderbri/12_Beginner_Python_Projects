# 08 Binary Search

This repository contains Python code showcasing the difference between naive search and binary search algorithms, demonstrating why binary search is a more efficient approach for finding elements in a sorted list.

## Naive Search

Naive search involves scanning the entire list sequentially and comparing each element with the target value. If the target is found, the index is returned; otherwise, -1 is returned. This approach has a time complexity of O(n), where n is the number of elements in the list.

## Binary Search

Binary search, on the other hand, utilizes the concept of divide and conquer. It takes advantage of the fact that the list is sorted and repeatedly divides the search interval in half until the target is found. This results in a significantly faster search time compared to naive search. Binary search has a time complexity of O(log n), making it much more efficient for large datasets.

## Code Explanation

The provided Python code includes implementations of both naive search and binary search algorithms. Here's a brief explanation of the code:

- **`naive_search`**: This function sequentially searches through the list `l` to find the `target` value. It returns the index if found, otherwise -1.

- **`binary_search`**: This function implements the binary search algorithm. It recursively divides the search interval in half until the `target` is found. It returns the index of the target if found, otherwise -1.

The main section of the code demonstrates the difference in performance between the two search algorithms. It generates a sorted list of random integers and measures the time taken by both naive search and binary search to search for each element in the list. The output displays the average time taken for each search algorithm.

To run the code and observe the performance difference, simply execute the Python script:
```bash
python3 binary_search.py
```

---
<p align="right">Completed: ２０２４年０３月０９日（土）</p>