# Python Memory Management - Quick Links

**[Reference Counting](#reference-counting)**  
Primary mechanism, `sys.getrefcount()`, del behavior

**[Garbage Collection](#garbage-collection)**  
Cycle detection, `gc` module, thresholds

**[Memory Allocators](#memory-allocators)**  
PyMalloc, raw malloc, arena/pool/bucket system

**[Object Memory Layout](#object-memory-layout)**  
PyObject header, `sys.getsizeof()`, overhead

**[Circular References](#circular-references)**  
Why refcount fails, GC triggers

**[Memory Views](#memory-views)**  
Zero-copy, `memoryview`, buffer protocol

**[Memory Optimization](#memory-optimization)**  
`__slots__`, small integer caching, string interning

---

## Reference Counting

### What is Reference Counting?
Reference counting is Python’s main way of keeping track of how many places (variables, containers, etc.) are using an object. When the count drops to zero, the memory is freed immediately.

### How It Works
- Every object has a reference count.
- When you assign an object to a new variable or put it in a list, the count goes up.
- When a reference is deleted, the count goes down.
- When the count reaches zero, Python deletes the object.

### Example
```python
import sys
x = []
print(sys.getrefcount(x))  # Usually 2 (one for x, one for getrefcount arg)
y = x
print(sys.getrefcount(x))  # Now 3

del y
print(sys.getrefcount(x))  # Back to 2
```

---

## Garbage Collection

### What is Garbage Collection?
Garbage collection (GC) is a backup system for cleaning up objects that reference each other in a cycle (so their refcounts never reach zero).

### How It Works
- Python’s `gc` module finds groups of objects that reference each other but are not used anywhere else.
- It runs automatically, but you can control it.

### Example
```python
import gc
print(gc.isenabled())  # True by default
# You can force a collection:
gc.collect()
```

---

## Memory Allocators

### What is a Memory Allocator?
A memory allocator is the part of Python that actually asks the operating system for memory and manages it efficiently for objects of different sizes.

### How It Works
- **PyMalloc:** Python’s custom allocator for small objects (fast and efficient).
- **Raw malloc:** Used for very large objects.
- **Arena/Pool/Bucket:** Memory is managed in chunks to reduce overhead and fragmentation.

---

## Object Memory Layout

### What is Object Memory Layout?
Every Python object has a header (with type info, refcount, etc.) and space for its data. This means even a tiny object uses more memory than just its value.

### How to Check Object Size
```python
import sys
print(sys.getsizeof(5))        # Size of an int
print(sys.getsizeof([]))       # Size of an empty list
print(sys.getsizeof(object())) # Size of a generic object
```

- The reported size does not include referenced objects (e.g., the contents of a list).

---

## Circular References

### What is a Circular Reference?
A circular reference happens when two or more objects reference each other, so their reference counts never reach zero.

### Why Is This a Problem?
Reference counting alone can’t clean up these objects, so the garbage collector is needed.

### Example
```python
class Node:
    def __init__(self):
        self.ref = None

a = Node()
b = Node()
a.ref = b
b.ref = a  # Now a and b reference each other
# Deleting a and b won’t free their memory unless GC runs
```

---

## Memory Views

### What is a Memory View?
A memory view lets you access the memory of another object (like a bytes or array) without copying it. This is useful for large data processing.

### Example
```python
data = bytearray(b'hello')
view = memoryview(data)
print(view[0])  # Output: 104 (ASCII for 'h')
view[0] = 72    # Change 'h' to 'H'
print(data)     # Output: bytearray(b'Hello')
```

---

## Memory Optimization

### How to Optimize Memory in Python
- **`__slots__`:** Prevents the creation of `__dict__` for each instance, saving memory.
- **Small Integer Caching:** Python reuses small integer objects (usually -5 to 256) for efficiency.
- **String Interning:** Python may reuse identical strings to save memory.

### Example: __slots__
```python
class Slim:
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y

s = Slim(1, 2)
# s.z = 3  # AttributeError: 'Slim' object has no attribute 'z'
```

---