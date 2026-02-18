# Python OOP - Quick Links

**[Classes & Instances](#classes--instances)**  
`class`, `__init__`, `self`, instance methods

**[Inheritance](#inheritance)**  
Single/multiple, super(), MRO (Method Resolution Order)

**[Magic Methods](#magic-methods)**  
`__str__`, `__repr__`, `__len__`, comparison operators

**[Operator Overloading](#operator-overloading)**  
`__add__`, `__eq__`, `__getitem__`, `__call__`

**[Properties & Decorators](#properties--decorators)**  
`@property`, `@<attr>.setter`, `@staticmethod`, `@classmethod`

**[Special Methods](#special-methods)**  
`__new__`, `__del__`, `__slots__` (memory optimization)

**[Abstract Base Classes](#abstract-base-classes)**  
`ABC`, `@abstractmethod`, interface enforcement

**[Dataclasses](#dataclasses)**  
`@dataclass` (3.7+), auto-generated methods

---


## Classes & Instances

A class is a blueprint for creating objects (instances). Each object can have its own data (attributes) and functions (methods).

### Defining a Class and Creating Instances
```python
class Dog:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age
    def bark(self):
        print(f"{self.name} says woof!")

# Creating instances
buddy = Dog("Buddy", 3)
luna = Dog("Luna", 5)

buddy.bark()  # Output: Buddy says woof!
luna.bark()   # Output: Luna says woof!
```

### How Are Classes and Instances Loaded in Memory?
- **Class Definition:** When Python executes the class definition, it creates a class object in memory.
- **Instance Creation:** Each time you call `Dog(...)`, Python allocates memory for a new object and links it to the class.
- **Attributes:** Instance attributes are stored in the instance’s `__dict__` (unless `__slots__` is used).

### Real-World Analogy
- **Class:** Like a car blueprint.
- **Instance:** Each car built from the blueprint (with its own color, engine, etc).

### More Examples
#### Instance Methods and Attributes
```python
class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []
    def enroll(self, course):
        self.courses.append(course)

s = Student("Alice")
s.enroll("Math")
print(s.courses)  # Output: ['Math']
```

---

## Object Size and Memory Usage

When you create an object, Python allocates memory for its basic structure. The size increases as you add attributes.

### Measuring Object Size
You can use the `sys.getsizeof()` function to check the size (in bytes) of an object. Note: This does not include referenced objects (like lists inside the object).

```python
import sys

class Empty:
    pass

class WithAttrs:
    def __init__(self):
        self.x = 10
        self.y = [1, 2, 3]

empty = Empty()
with_attrs = WithAttrs()

print(sys.getsizeof(empty))      # Size of empty instance
print(sys.getsizeof(with_attrs)) # Size with attributes
print(sys.getsizeof(with_attrs.y)) # Size of the list attribute
```

- **Adding attributes increases the size of the instance’s `__dict__`.**
- **For memory optimization, use `__slots__` to prevent dynamic attribute creation.**

---

## Inheritance

Inheritance lets you create a new class (child) that reuses, extends, or modifies the behavior of another class (parent).

### Single Inheritance Example
```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

d = Dog()
d.speak()  # Output: Dog barks
```

### Multiple Inheritance Example
```python
class Swimmer:
    def swim(self):
        print("Swimming...")

class Flyer:
    def fly(self):
        print("Flying...")

class Duck(Swimmer, Flyer):
    pass

d = Duck()
d.swim()  # Output: Swimming...
d.fly()   # Output: Flying...
```

### Using super() and MRO
- `super()` lets you call methods from a parent class.
- MRO (Method Resolution Order) determines the order in which base classes are searched.

```python
class A:
    def do(self):
        print("A")
class B(A):
    def do(self):
        print("B")
        super().do()
class C(B):
    def do(self):
        print("C")
        super().do()

c = C()
c.do()  # Output: C B A
```

### Real-World Analogy
- **Inheritance:** Like a child inheriting traits from parents.
- **Multiple inheritance:** Like inheriting skills from both mom and dad.

---

## Magic Methods

Magic methods (dunder methods) are special methods with double underscores, used to define how objects behave with built-in operations.

### Common Magic Methods
```python
class Book:
    def __init__(self, title):
        self.title = title
    def __str__(self):
        return f"Book: {self.title}"
    def __len__(self):
        return len(self.title)

b = Book("Python 101")
print(str(b))      # Output: Book: Python 101
print(len(b))      # Output: 10
```

### Real-World Analogy
- **Magic methods:** Like customizing how your object responds to built-in questions ("How long are you?", "What do you look like as a string?").

---

## Operator Overloading

Operator overloading lets you define how operators like +, ==, [] work for your objects.

### Example: __add__ and __eq__
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3.x, p3.y)  # Output: 4 6
print(p1 == p2)    # Output: False
```

### Real-World Analogy
- **Operator overloading:** Like teaching your objects how to add, compare, or access themselves in custom ways.

---

## Properties & Decorators

Properties and decorators let you control access to attributes and define class/instance/static methods.

### @property Example
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius must be positive!")
        self._radius = value

c = Circle(5)
c.radius = 10
print(c.radius)  # Output: 10
```

### @staticmethod and @classmethod
```python
class Math:
    @staticmethod
    def add(x, y):
        return x + y
    @classmethod
    def description(cls):
        return f"This is {cls.__name__} class"

print(Math.add(2, 3))           # Output: 5
print(Math.description())       # Output: This is Math class
```

---

## Special Methods

Special methods like `__new__`, `__del__`, and `__slots__` control object creation, destruction, and memory usage.

### __new__ and __del__
```python
class MyClass:
    def __new__(cls, *args, **kwargs):
        print("Allocating memory for new object")
        return super().__new__(cls)
    def __init__(self):
        print("Initializing object")
    def __del__(self):
        print("Object is being destroyed")

obj = MyClass()
del obj
```

### __slots__ for Memory Optimization
```python
class Slim:
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y

s = Slim(1, 2)
# s.z = 3  # AttributeError: 'Slim' object has no attribute 'z'
```
- **Using `__slots__` saves memory by preventing the creation of `__dict__` for each instance.**

---

## Abstract Base Classes

Abstract Base Classes (ABCs) let you define methods that must be created within any child classes built from the abstract base class.

### Example
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

d = Dog()
d.make_sound()  # Output: Woof!
```

---

## Dataclasses

Dataclasses automatically generate special methods like `__init__`, `__repr__`, and `__eq__` for classes with attributes.

### Example
```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1)         # Output: Point(x=1, y=2)
print(p1 == p2)   # Output: True
```

---