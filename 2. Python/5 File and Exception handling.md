# File & Exception Handling - Quick Links

**[Exception Hierarchy](#exception-hierarchy)**  
BaseException → Exception → built-ins (ValueError, TypeError...)

**[Try-Except Blocks](#try-except-blocks)**  
Basic handling, multiple except, else/finally

**[Raising Exceptions](#raising-exceptions)**  
raise, assert, custom exception classes

**[File I/O Basics](#file-io-basics)**  
open(), read/write modes, with statement

**[Context Managers](#context-managers)**  
with statement, file handling best practice

**[Custom Exceptions](#custom-exceptions)**  
Class-based exceptions, inheritance

**[Advanced File Ops](#advanced-file-ops)**  
Binary I/O, seek/tell, pathlib (modern)

---

## Exception Hierarchy

Python exceptions are organized in a hierarchy, starting from `BaseException`. Most errors you handle inherit from `Exception`.

### Visual Hierarchy
```
BaseException
 ├── SystemExit
 ├── KeyboardInterrupt
 └── Exception
      ├── ArithmeticError
      │    ├── ZeroDivisionError
      │    └── OverflowError
      ├── ValueError
      ├── TypeError
      ├── FileNotFoundError
      └── ... (many more)
```

### Example
```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
```

### Real-World Analogy
Think of exceptions like different types of alarms in a building:
- **BaseException**: The main alarm system.
- **Exception**: Everyday alarms (fire, burglary).
- **SystemExit/KeyboardInterrupt**: Special alarms (power cut, manual override).

---

## Try-Except Blocks

Try-except blocks let you handle errors gracefully, so your program doesn't crash unexpectedly.

### Basic Structure
```python
try:
    # Code that might cause an error
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

### Handling Multiple Exceptions
```python
try:
    value = int("abc")
    result = 10 / value
except ValueError:
    print("Could not convert to integer!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

### Using else and finally
- **else:** Runs if no exception occurs.
- **finally:** Always runs (cleanup, closing files, etc).

```python
try:
    f = open("data.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("File not found!")
else:
    print("File read successfully.")
finally:
    print("This always runs.")
```

### Real-World Analogy
Like trying to unlock a door:
- **try:** Insert the key.
- **except:** If the key breaks, handle the problem.
- **else:** If it opens, walk in.
- **finally:** Always lock the door when leaving.

---

## Raising Exceptions

You can raise exceptions manually to signal errors in your code.

### Using raise
```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds!")
    return balance - amount

try:
    withdraw(100, 150)
except ValueError as e:
    print(e)  # Output: Insufficient funds!
```

### Using assert
```python
x = -5
assert x >= 0, "x must be non-negative!"
# Raises AssertionError: x must be non-negative!
```

### Custom Exception Classes
```python
class NegativeNumberError(Exception):
    pass

def check_positive(x):
    if x < 0:
        raise NegativeNumberError("Negative number not allowed!")

try:
    check_positive(-10)
except NegativeNumberError as e:
    print(e)
```

---

## File I/O Basics

File I/O (Input/Output) lets you read from and write to files.

### Opening and Reading Files
```python
# Open a file for reading
f = open("example.txt", "r")
content = f.read()
print(content)
f.close()
```

### Writing to Files
```python
# Open a file for writing
f = open("output.txt", "w")
f.write("Hello, world!\n")
f.close()
```

### Using with Statement (Best Practice)
```python
with open("example.txt", "r") as f:
    for line in f:
        print(line.strip())
```

---

## Context Managers

Context managers handle setup and cleanup actions automatically (like opening/closing files).

### File Handling Example
```python
with open("data.txt", "w") as f:
    f.write("Data saved!\n")
# File is closed automatically here
```

### Custom Context Manager
```python
class ManagedFile:
    def __init__(self, filename):
        self.filename = filename
    def __enter__(self):
        self.file = open(self.filename, "w")
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with ManagedFile("myfile.txt") as f:
    f.write("Hello from custom context manager!\n")
```

### Real-World Analogy
Like borrowing a library book:
- **enter:** Check out the book.
- **exit:** Return the book (even if you spill coffee on it).

---

## Custom Exceptions

You can define your own exceptions for specific error cases in your application.

### Example
```python
class AgeTooSmallError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise AgeTooSmallError("Age must be at least 18!")

try:
    check_age(15)
except AgeTooSmallError as e:
    print(e)
```

### Real-World Analogy
Like creating a custom warning sign for a unique hazard in your workplace.

---

## Advanced File Ops

Advanced file operations include binary I/O, file pointer movement, and using modern libraries like pathlib.

### Binary I/O
```python
# Write bytes to a file
with open("data.bin", "wb") as f:
    f.write(b"\x00\xFF\x10")

# Read bytes from a file
with open("data.bin", "rb") as f:
    data = f.read()
    print(data)
```

### seek() and tell()
```python
with open("example.txt", "r") as f:
    print(f.tell())  # Current position
    f.seek(5)        # Move to position 5
    print(f.read())  # Read from position 5
```

### Using pathlib (Modern File Handling)
```python
from pathlib import Path

file = Path("example.txt")
if file.exists():
    print(file.read_text())
else:
    file.write_text("Created with pathlib!\n")
```

### Real-World Analogy
- **Binary I/O:** Like sending/receiving secret codes instead of plain text.
- **seek/tell:** Like moving a bookmark in a book to jump to a specific page.
- **pathlib:** Like using a GPS instead of a paper map for file navigation.

---

## More Exception Examples

Here are more examples of common Python exceptions:

### TypeError
```python
try:
    result = '2' + 3
except TypeError as e:
    print(f"TypeError: {e}")
```

### IndexError
```python
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError as e:
    print(f"IndexError: {e}")
```

### KeyError
```python
try:
    d = {'a': 1}
    print(d['b'])
except KeyError as e:
    print(f"KeyError: {e}")
```

### FileNotFoundError
```python
try:
    with open('nofile.txt', 'r') as f:
        f.read()
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")
```

### ValueError
```python
try:
    num = int('hello')
except ValueError as e:
    print(f"ValueError: {e}")
```

---
