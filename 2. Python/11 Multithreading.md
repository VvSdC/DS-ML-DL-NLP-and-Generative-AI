# Multi-threading & Multi-processing - Quick Links

**[Threading Basics](#threading-basics)**  
`threading.Thread`, daemon threads, GIL impact

**[Locks & Synchronization](#locks--synchronization)**  
Lock, RLock, Semaphore, Condition, Event

**[Threading Patterns](#threading-patterns)**  
Thread pools (concurrent.futures), producer-consumer

**[Multiprocessing](#multiprocessing)**  
`multiprocessing.Process`, Pool, shared memory

**[Process vs Thread](#process-vs-thread)**  
CPU-bound vs I/O-bound, GIL bypass, overhead

**[Asyncio](#asyncio)**  
`async def`, `await`, event loop (non-blocking I/O)

**[Concurrent.futures](#concurrentfutures)**  
ThreadPoolExecutor, ProcessPoolExecutor, as_completed

---

## Threading Basics

### What is a Thread?
A thread is a separate flow of execution within a program. Multiple threads can run "at the same time" (concurrently) in the same process, sharing memory and resources.

### Why Use Threads?
- To perform multiple tasks at once (e.g., downloading files while updating the UI).
- To keep programs responsive during I/O operations (like reading files or network requests).

### Key Terms
- **Main Thread:** The original thread that starts when your program runs.
- **Child Thread:** Any thread you create in addition to the main thread.
- **Daemon Thread:** A thread that runs in the background and does not block program exit.
- **GIL (Global Interpreter Lock):** A mechanism in CPython that allows only one thread to execute Python bytecode at a time. This means threads are best for I/O-bound, not CPU-bound, tasks in standard Python.

### Creating and Starting Threads
```python
import threading

def print_numbers():
    for i in range(3):
        print(f"Number: {i}")

# Create a thread
t = threading.Thread(target=print_numbers)
# Start the thread
t.start()
# Wait for the thread to finish
t.join()
print("Done!")
# Output:
# Number: 0
# Number: 1
# Number: 2
# Done!
```

### Daemon Threads
```python
import threading
import time

def background_task():
    while True:
        print("Running in background...")
        time.sleep(1)

t = threading.Thread(target=background_task, daemon=True)
t.start()
time.sleep(2)
print("Main program ends, daemon thread will be killed.")
# Output:
# Running in background...
# Running in background...
# Main program ends, daemon thread will be killed.
```

---

## Locks & Synchronization

### What is Synchronization?
Synchronization is making sure that only one thread accesses a shared resource (like a variable or file) at a time, to prevent data corruption.

### Key Terms
- **Lock:** A basic mechanism to prevent multiple threads from accessing a resource at the same time.
- **RLock (Reentrant Lock):** Like a Lock, but the same thread can acquire it multiple times.
- **Semaphore:** Allows a fixed number of threads to access a resource.
- **Condition:** Lets threads wait for certain conditions to be met.
- **Event:** A flag that threads can wait for or set.

### Lock Example
```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(1000):
        with lock:
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(10)]
for t in threads: t.start()
for t in threads: t.join()
print(counter)  # Output: 10000
```

### Semaphore Example
```python
import threading
import time

sem = threading.Semaphore(2)

def task(n):
    with sem:
        print(f"Thread {n} running")
        time.sleep(1)

for i in range(4):
    threading.Thread(target=task, args=(i,)).start()
# Only 2 threads run at a time
```

---

## Threading Patterns

### Thread Pool
A thread pool manages a group of worker threads to perform many tasks efficiently.

```python
from concurrent.futures import ThreadPoolExecutor

def square(n):
    return n * n

with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(square, [1, 2, 3, 4, 5]))
print(results)  # Output: [1, 4, 9, 16, 25]
```

### Producer-Consumer Pattern
This pattern separates the creation of data (producer) from its processing (consumer), often using a queue.

```python
import threading
import queue
import time

q = queue.Queue()

def producer():
    for i in range(5):
        print(f"Produced {i}")
        q.put(i)
        time.sleep(0.5)

def consumer():
    while True:
        item = q.get()
        print(f"Consumed {item}")
        q.task_done()

threading.Thread(target=producer).start()
threading.Thread(target=consumer, daemon=True).start()
q.join()
```

---

## Multiprocessing

### What is Multiprocessing?
Multiprocessing runs code in separate processes, each with its own memory space. This bypasses the GIL and is good for CPU-bound tasks.

### Key Terms
- **Process:** Like a thread, but runs in a separate memory space.
- **Pool:** A group of worker processes.
- **Shared Memory:** Mechanisms to share data between processes (e.g., `Value`, `Array`).

### Basic Process Example
```python
from multiprocessing import Process

def f(name):
    print(f"Hello {name}")

p = Process(target=f, args=("World",))
p.start()
p.join()
```

### Pool Example
```python
from multiprocessing import Pool

def square(n):
    return n * n

with Pool(4) as pool:
    results = pool.map(square, [1, 2, 3, 4])
print(results)  # Output: [1, 4, 9, 16]
```

---

## Process vs Thread

### Key Differences
- **Threads** share memory, are lightweight, and are best for I/O-bound tasks (like waiting for files or network).
- **Processes** have separate memory, are heavier, and are best for CPU-bound tasks (like calculations).
- **GIL (Global Interpreter Lock):** Only one thread runs Python code at a time in CPython, but each process runs independently.

### When to Use Each
- Use **threads** for tasks that spend time waiting (I/O-bound).
- Use **processes** for tasks that use a lot of CPU (CPU-bound).

---

## Asyncio

### What is asyncio?
`asyncio` is a library for writing single-threaded, concurrent code using coroutines, making it easy to handle many I/O-bound tasks at once.

### Key Terms
- **Coroutine:** A special function you can pause and resume with `await`.
- **Event Loop:** The core of asyncio, runs and manages all coroutines.
- **await:** Tells Python to pause here and let other tasks run.

### Basic asyncio Example
```python
import asyncio

async def main():
    print('Hello')
    await asyncio.sleep(1)
    print('World')

asyncio.run(main())
# Output:
# Hello
# (waits 1 second)
# World
```

---

## Concurrent.futures

### What is concurrent.futures?
A high-level module for running tasks in threads or processes, with a simple interface.

### Key Terms
- **ThreadPoolExecutor:** Runs tasks in threads.
- **ProcessPoolExecutor:** Runs tasks in processes.
- **as_completed:** Lets you process results as soon as each task finishes.

### Example: ThreadPoolExecutor
```python
from concurrent.futures import ThreadPoolExecutor, as_completed

def work(x):
    return x * 2

with ThreadPoolExecutor(max_workers=2) as executor:
    futures = [executor.submit(work, i) for i in range(4)]
    for future in as_completed(futures):
        print(future.result())
```

### Example: ProcessPoolExecutor
```python
from concurrent.futures import ProcessPoolExecutor

def work(x):
    return x * x

with ProcessPoolExecutor(max_workers=2) as executor:
    results = list(executor.map(work, [1, 2, 3, 4]))
print(results)  # Output: [1, 4, 9, 16]
```

---
