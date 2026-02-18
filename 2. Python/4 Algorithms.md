# Python Algorithms - Quick Links

**[Linear Search](#linear-search)**  
Sequential scan, O(n) time

**[Binary Search](#binary-search)**  
Sorted array, O(log n), bisect module

**[Bubble Sort](#bubble-sort)**  
Adjacent swaps, O(n²), stable

**[Selection Sort](#selection-sort)**  
Min selection, O(n²), simple

**[Insertion Sort](#insertion-sort)**  
Build sorted prefix, O(n²) best for small

**[Merge Sort](#merge-sort)**  
Divide-conquer-merge, O(n log n), stable

**[Quick Sort](#quick-sort)**  
Partition around pivot, O(n log n) average

**[Complexity Cheat Sheet](#complexity-cheat-sheet)**  
Big-O notation reference

**[Built-in sorting](#built-in-sorting)**
sorted(iterable, key=..., reverse=False) # Stable TimSort O(n log n)
list.sort() # In-place TimSort

---

## Linear Search

Linear search scans each element in a list one by one to find a target value.

### Time and Space Complexity
| Case      | Time Complexity | Space Complexity |
|-----------|----------------|-----------------|
| Best      | O(1)           | O(1)            |
| Average   | O(n)           | O(1)            |
| Worst     | O(n)           | O(1)            |

- **Best Case:** Target is the first element.
- **When to Use:**
  - The list is unsorted or very small.
  - Simplicity is more important than speed.

### Python Code Example
```python
def linear_search(arr, target):
    """
    Searches for 'target' in 'arr' using linear search.
    Returns the index if found, else -1.
    """
    for index, value in enumerate(arr):
        if value == target:
            return index  # Found the target
    return -1  # Target not found

# Example usage:
numbers = [4, 2, 7, 1, 9]
result = linear_search(numbers, 7)
print(f"7 found at index: {result}")  # Output: 7 found at index: 2
```

### Real-World Example
- **Finding a contact in a small, unsorted phone list.**
- **Checking attendance by calling out each name in a class list.**

---

## Binary Search

Binary search efficiently finds a target value in a sorted list by repeatedly dividing the search interval in half.

### Time and Space Complexity
| Case      | Time Complexity | Space Complexity |
|-----------|----------------|-----------------|
| Best      | O(1)           | O(1)            |
| Average   | O(log n)       | O(1)            |
| Worst     | O(log n)       | O(1)            |

- **Best Case:** Target is at the middle of the list.
- **When to Use:**
  - The list is sorted.
  - Fast lookups are needed.

### Python Code Example
```python
def binary_search(arr, target):
    """
    Searches for 'target' in sorted 'arr' using binary search.
    Returns the index if found, else -1.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage:
numbers = [1, 2, 4, 7, 9]
result = binary_search(numbers, 7)
print(f"7 found at index: {result}")  # Output: 7 found at index: 3
```

### Real-World Example
- **Looking up a word in a dictionary.**
- **Finding a name in a sorted contact list.**

---

## Bubble Sort

Bubble sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

### Time and Space Complexity
| Case      | Time Complexity | Space Complexity |
|-----------|----------------|-----------------|
| Best      | O(n)           | O(1)            |
| Average   | O(n²)          | O(1)            |
| Worst     | O(n²)          | O(1)            |

- **Best Case:** List is already sorted.
- **When to Use:**
  - Educational purposes or very small lists.
  - When simplicity is more important than efficiency.

### Python Code Example
```python
def bubble_sort(arr):
    """
    Sorts 'arr' in place using bubble sort.
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # Stop if already sorted

# Example usage:
numbers = [5, 1, 4, 2, 8]
bubble_sort(numbers)
print(numbers)  # Output: [1, 2, 4, 5, 8]
```

### Real-World Example
- **Sorting a small list of test scores by hand.**
- **Teaching sorting concepts to beginners.**

---

## Selection Sort

Selection sort repeatedly finds the minimum element from the unsorted part and puts it at the beginning.

### Time and Space Complexity
| Case      | Time Complexity | Space Complexity |
|-----------|----------------|-----------------|
| Best      | O(n²)          | O(1)            |
| Average   | O(n²)          | O(1)            |
| Worst     | O(n²)          | O(1)            |

- **Best Case:** All cases are O(n²); no best-case improvement.
- **When to Use:**
  - Small lists where memory writes are costly (few swaps).
  - Simplicity is desired.

### Python Code Example
```python
def selection_sort(arr):
    """
    Sorts 'arr' in place using selection sort.
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Example usage:
numbers = [64, 25, 12, 22, 11]
selection_sort(numbers)
print(numbers)  # Output: [11, 12, 22, 25, 64]
```

### Real-World Example
- **Selecting the lightest item from a group repeatedly.**
- **Arranging books by height one by one.**

---

## Insertion Sort

Insertion sort builds the sorted array one item at a time by inserting each element into its correct position.

### Time and Space Complexity
| Case      | Time Complexity | Space Complexity |
|-----------|----------------|-----------------|
| Best      | O(n)           | O(1)            |
| Average   | O(n²)          | O(1)            |
| Worst     | O(n²)          | O(1)            |

- **Best Case:** List is already sorted.
- **When to Use:**
  - Small or nearly sorted lists.
  - Online sorting (as data arrives).

### Python Code Example
```python
def insertion_sort(arr):
    """
    Sorts 'arr' in place using insertion sort.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage:
numbers = [12, 11, 13, 5, 6]
insertion_sort(numbers)
print(numbers)  # Output: [5, 6, 11, 12, 13]
```

### Real-World Example
- **Sorting playing cards in your hand.**
- **Arranging files by date as you receive them.**

---

## Merge Sort

Merge sort is a divide-and-conquer algorithm that splits the list into halves, sorts each half, and merges them back together.

### Time and Space Complexity
| Case      | Time Complexity | Space Complexity |
|-----------|----------------|-----------------|
| Best      | O(n log n)     | O(n)            |
| Average   | O(n log n)     | O(n)            |
| Worst     | O(n log n)     | O(n)            |

- **Best Case:** All cases are O(n log n); stable sort.
- **When to Use:**
  - Large lists where stability is required.
  - Linked lists (can be done in O(1) space).

### Python Code Example
```python
def merge_sort(arr):
    """
    Sorts 'arr' using merge sort and returns a new sorted list.
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example usage:
numbers = [38, 27, 43, 3, 9, 82, 10]
sorted_numbers = merge_sort(numbers)
print(sorted_numbers)  # Output: [3, 9, 10, 27, 38, 43, 82]
```

### Real-World Example
- **Merging two sorted mailing lists.**
- **Sorting large datasets in external storage.**

---

## Quick Sort

Quick sort picks a 'pivot' element and partitions the array into elements less than and greater than the pivot, then recursively sorts the partitions.

### Time and Space Complexity
| Case      | Time Complexity | Space Complexity |
|-----------|----------------|-----------------|
| Best      | O(n log n)     | O(log n)        |
| Average   | O(n log n)     | O(log n)        |
| Worst     | O(n²)          | O(log n)        |

- **Best Case:** Pivot always splits the list evenly.
- **When to Use:**
  - Large lists where average performance is more important than worst-case.
  - In-place sorting is needed.

### Python Code Example
```python
def quick_sort(arr):
    """
    Sorts 'arr' using quick sort and returns a new sorted list.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Example usage:
numbers = [10, 7, 8, 9, 1, 5]
sorted_numbers = quick_sort(numbers)
print(sorted_numbers)  # Output: [1, 5, 7, 8, 9, 10]
```

### Real-World Example
- **Organizing large sets of records in databases.**
- **Sorting files by size or date quickly.**

---

