# Python Advanced Concepts - Quick Links

**[Decorators](#decorators)**  
Function/class decorators, `@wraps`, parameter preservation

**[Generators](#generators)**  
`yield`, generator expressions, send()/throw()

**[Iterators](#iterators)**  
`__iter__`/`__next__`, custom iteration protocol

**[Context Managers](#context-managers)**  
`@contextmanager`, `__enter__`/`__exit__`

**[Closures](#closures)**  
Nested functions, `nonlocal`, function factories

**[Metaclasses](#metaclasses)**  
`type`, custom `__new__`, class creation control

**[Descriptors](#descriptors)**  
`__get__`/`__set__`/`__delete__`, property implementation

**[Async/Await Preview](#asyncawait-preview)**  
`async def`, `await`, coroutines basics

## Decorators

### What is a Decorator?
A decorator is a function that takes another function (or class) and extends or changes its behavior without modifying its code. Decorators are a powerful way to add reusable features to functions or methods.

### When to Use Decorators?
- When you want to add the same functionality (like logging, timing, access control) to many functions without repeating code.
- When you want to separate "what a function does" from "how it is used" (e.g., caching, validation).

### Real-World Analogy
Think of a decorator like a gift wrapper: you can wrap any present (function) to add a new look (feature) without changing the gift itself.

### Basic Function Decorator Example
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function runs")
        result = func(*args, **kwargs)
        print("After the function runs")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before the function runs
# Hello!
# After the function runs
```

### Using @wraps to Preserve Metadata
```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

### Decorators with Arguments
```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hi!")

greet()
# Output:
# Hi!
# Hi!
# Hi!
```

## Generators

### What is a Generator?
A generator is a special type of function that lets you yield values one at a time, pausing between each, instead of returning them all at once. Generators use the `yield` keyword.

### When to Use Generators?
- When you want to process large data sets without loading everything into memory.
- When you want to create pipelines or streams of data.

### Real-World Analogy
A generator is like a water tap: you get water (data) only when you turn the tap (iterate), not all at once.

### Basic Generator Example
```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(3):
    print(num)
# Output:
# 1
# 2
# 3
```

### Generator Expressions
```python
gen = (x * x for x in range(4))
for val in gen:
    print(val)
# Output: 0 1 4 9
```

## Iterators

### What is an Iterator?
An iterator is an object that lets you loop over a collection, one item at a time. It implements the `__iter__()` and `__next__()` methods.

### When to Use Iterators?
- When you want to create custom objects that can be looped over with `for`.
- When you want to control how iteration works (e.g., skipping, filtering).

### Real-World Analogy
An iterator is like a TV remote: you press "next" to get the next channel (item).

### Custom Iterator Example
```python
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

for num in Counter(1, 3):
    print(num)
# Output:
# 1
# 2
# 3
```

## Context Managers

### What is a Context Manager?
A context manager is a Python object that sets something up and then cleans it up automatically. The most common use is with the `with` statement (like opening files).

### When to Use Context Managers?
- When you need to manage resources (files, network connections) and ensure they are cleaned up properly.
- When you want to guarantee setup/teardown code runs, even if there’s an error.

### Real-World Analogy
A context manager is like borrowing a library book: you check it out (setup), use it, and return it (cleanup), even if you spill coffee on it (error).

### Basic Context Manager Example
```python
with open('example.txt', 'w') as f:
    f.write('Hello!')
# File is closed automatically
```

### Custom Context Manager with Class
```python
class ManagedFile:
    def __init__(self, filename):
        self.filename = filename
    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with ManagedFile('myfile.txt') as f:
    f.write('Hi!')
```

### Using @contextmanager Decorator
```python
from contextlib import contextmanager

@contextmanager
def managed_resource():
    print('Setup')
    yield 'resource'
    print('Cleanup')

with managed_resource() as res:
    print('Using', res)
# Output:
# Setup
# Using resource
# Cleanup
```

## Closures

### What is a Closure?
A closure is a function defined inside another function that remembers the values from the enclosing scope, even after the outer function has finished.

### When to Use Closures?
- When you want to create function factories (functions that generate other functions with preset data).
- When you want to keep some data private and persistent between calls.

### Real-World Analogy
A closure is like a backpack: you pack it with things (variables) and carry it with you (the inner function remembers them).

### Closure Example
```python
def make_multiplier(x):
    def multiplier(n):
        return x * n
    return multiplier

double = make_multiplier(2)
print(double(5))  # Output: 10
```

### Using nonlocal
```python
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c = counter()
print(c())  # Output: 1
print(c())  # Output: 2
```

## Metaclasses

### What is a Metaclass?
A metaclass is a "class of a class"—it controls how classes are created. Most people never need to write one, but they are powerful for advanced customization.

### When to Use Metaclasses?
- When you want to automatically modify or register classes as they are created.
- When you want to enforce rules or inject methods into classes.

### Real-World Analogy
A metaclass is like a factory that builds blueprints (classes), not just the products (objects).

### Basic Metaclass Example
```python
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f'Creating class {name}')
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta):
    pass
# Output: Creating class MyClass
```

## Descriptors

### What is a Descriptor?
A descriptor is an object attribute with special methods (`__get__`, `__set__`, `__delete__`) that lets you customize what happens when you access, set, or delete an attribute.

### When to Use Descriptors?
- When you want to manage attribute access (validation, computed properties, etc).
- When you want to implement reusable property logic.

### Real-World Analogy
A descriptor is like a smart lock: it controls how you open, close, or remove a door (attribute).

### Descriptor Example
```python
class Positive:
    def __get__(self, instance, owner):
        return instance._value
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Must be positive!')
        instance._value = value

class Number:
    value = Positive()
    def __init__(self, value):
        self.value = value

n = Number(5)
print(n.value)  # Output: 5
n.value = -2    # Raises ValueError
```

## Async/Await Preview

### What is async/await?
`async` and `await` are keywords for writing asynchronous code—code that can pause and let other code run while waiting for something (like a web request or file read).

### When to Use async/await?
- When you want to write code that does many things at once (concurrent tasks).
- When you want to avoid blocking your program while waiting for slow operations.

### Real-World Analogy
Async/await is like ordering food at a restaurant: you place your order (start a task), then do something else (other tasks) while you wait for your food (result).

### Basic async/await Example
```python
import asyncio

async def greet():
    print('Hello')
    await asyncio.sleep(1)
    print('World')

asyncio.run(greet())
# Output:
# Hello
# (waits 1 second)
# World
```

