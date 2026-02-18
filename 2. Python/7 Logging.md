# Python Logging - Quick Links

**[Logging Basics](#logging-basics)**  
`logging` module, levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)

**[Configuration](#configuration)**  
BasicConfig, dictConfig, fileConfig, logging.conf

**[Loggers, Handlers, Formatters](#loggers-handlers-formatters)**  
Logger hierarchy, Handler types, Formatter syntax

**[Rotating Logs](#rotating-logs)**  
TimedRotatingFileHandler, RotatingFileHandler

**[Structured Logging](#structured-logging)**  
JSON formatting, extra fields, loguru alternative

**[Best Practices](#best-practices)**  
Levels correctly, avoid print(), context logging

**[Filters & Propagation](#filters--propagation)**  
Custom filters, logger propagation control

---

## Logging Basics

Logging is a way for your program to report events, errors, or information while it runs. Unlike print statements, logs can be filtered by importance, saved to files, and formatted for easy reading.

### Why Use Logging?
Logging helps you:
- Debug and monitor your code.
- Keep a record of what happened and when.
- Turn logging on/off or redirect it to files easily.

### What is the logging module?
Python’s built-in `logging` module provides a flexible way to log messages from your code. It’s more powerful than using `print()` because you can control what gets logged, where it goes, and how it looks.

### Logging Levels
Logging levels let you categorize messages by importance:
- **DEBUG**: Detailed information, for diagnosing problems.
- **INFO**: Confirmation that things are working as expected.
- **WARNING**: Something unexpected happened, but the program is still running.
- **ERROR**: A serious problem, the program might not be able to continue.
- **CRITICAL**: A very serious error, program may crash.

### Basic Logging Example
The following code shows how to use the logging module and what gets printed at each level:
```python
import logging

# Set up basic logging
logging.basicConfig(level=logging.DEBUG)

logging.debug("This is a debug message")      # Printed: for debugging
logging.info("This is an info message")        # Printed: for general info
logging.warning("This is a warning message")   # Printed: something unexpected
logging.error("This is an error message")      # Printed: a serious problem
logging.critical("This is a critical message") # Printed: very serious error
```

#### Output (all messages printed because level=DEBUG):
```
DEBUG:root:This is a debug message
INFO:root:This is an info message
WARNING:root:This is a warning message
ERROR:root:This is an error message
CRITICAL:root:This is a critical message
```

### What Happens If You Change the Level?
If you set the logging level higher, only more important messages are shown:
```python
import logging
logging.basicConfig(level=logging.WARNING)

logging.debug("Debug")    # Not printed
logging.info("Info")      # Not printed
logging.warning("Warn")   # Printed
logging.error("Error")    # Printed
```

#### Output:
```
WARNING:root:Warn
ERROR:root:Error
```

---

## Configuration

Before you can use logging effectively, you need to configure it. Configuration means telling Python where to send log messages (console, file, etc.), what level to show, and how the messages should look.

### Ways to Configure Logging
- **basicConfig:** Easiest way for small scripts. Sets up logging in one line.
- **fileConfig/dictConfig:** For bigger projects, lets you use config files or dictionaries for more control.

### Example: basicConfig
This sets the minimum level and the message format:
```python
import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')
logging.info('Hello!')  # Output: INFO:Hello!
```

### Logging to a File
You can save logs to a file instead of printing them to the screen:
```python
import logging
logging.basicConfig(filename='app.log', level=logging.ERROR)
logging.error('This goes to the file!')
# No output on screen, but 'app.log' will contain: ERROR:root:This goes to the file!
```

### Advanced: dictConfig and fileConfig
For large projects, you can use a config file or dictionary to set up multiple loggers, handlers, and formatters. (See the official docs for details.)

---

## Loggers, Handlers, Formatters

Logging is built from three main parts:
- **Logger:** The main object you use to write logs. You can have many loggers in a big project.
- **Handler:** Decides where the log goes (console, file, email, etc). You can add multiple handlers to a logger.
- **Formatter:** Controls how the log message looks (timestamp, level, message, etc).

### How They Work Together
When you log a message, it goes to a logger. The logger sends it to its handlers. Each handler formats the message and sends it to its destination.

### Example: Custom Logger with Handlers and Formatter
```python
import logging

logger = logging.getLogger('myapp')
logger.setLevel(logging.DEBUG)

# Handler for console
console = logging.StreamHandler()
console.setLevel(logging.INFO)

# Handler for file
file = logging.FileHandler('myapp.log')
file.setLevel(logging.ERROR)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
file.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(console)
logger.addHandler(file)

logger.debug('Debug')    # Not printed (console needs INFO+)
logger.info('Info')      # Printed to console
logger.error('Error!')   # Printed to console and written to file
```

#### Output on console:
```
YYYY-MM-DD HH:MM:SS,sss - INFO - Info
YYYY-MM-DD HH:MM:SS,sss - ERROR - Error!
```

#### Output in 'myapp.log':
```
YYYY-MM-DD HH:MM:SS,sss - ERROR - Error!
```

---

## Rotating Logs

If your program runs for a long time, log files can get huge. Rotating logs means creating new files when the old one gets too big or too old, so you don’t fill up your disk.

### Types of Rotating Handlers
- **RotatingFileHandler:** Rotates when the file reaches a certain size.
- **TimedRotatingFileHandler:** Rotates after a certain time (e.g., every day).

### Example: RotatingFileHandler
This creates a new file when the log reaches 100 bytes, keeping 2 backups:
```python
import logging
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler('rotating.log', maxBytes=100, backupCount=2)
logging.basicConfig(handlers=[handler], level=logging.INFO)

for i in range(20):
    logging.info(f'Log entry {i}')
# When 'rotating.log' reaches 100 bytes, it rotates to 'rotating.log.1', etc.
```

### Example: TimedRotatingFileHandler
This rotates the log every 5 seconds:
```python
import logging
from logging.handlers import TimedRotatingFileHandler

handler = TimedRotatingFileHandler('timed.log', when='s', interval=5, backupCount=2)
logging.basicConfig(handlers=[handler], level=logging.INFO)

logging.info('This will rotate every 5 seconds')
```

---

## Structured Logging

Structured logging means logging in a format that’s easy for computers to parse (like JSON), not just plain text. This is useful for big systems and log analysis tools.

### Why Use Structured Logging?
- Makes it easier to search, filter, and analyze logs.
- Lets you add extra fields (like user, request id) to each log.

### Example: JSON Logging
This example logs messages as JSON objects:
```python
import logging
import json

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            'level': record.levelname,
            'message': record.getMessage(),
            'time': self.formatTime(record)
        }
        return json.dumps(log_record)

handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())
logger = logging.getLogger('jsonLogger')
logger.addHandler(handler)
logger.setLevel(logging.INFO)

logger.info('Structured log!')
# Output: {"level": "INFO", "message": "Structured log!", "time": "..."}
```

### Adding Extra Fields
You can add custom fields to your logs for more context:
```python
logger.info('User logged in', extra={'user': 'alice'})
```

---

## Best Practices

Here are some tips for using logging well:
- Use the right log level (don’t log everything as ERROR).
- Don’t use print() for real applications—use logging.
- Add context (like user, request id) to logs.
- Use rotating logs for production.
- Never log sensitive info (passwords, etc).

### Example: Context Logging
You can add extra information to your logs for better debugging:
```python
import logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s')
logging.info('User login', extra={'user': 'bob'})
```

---

## Filters & Propagation

Filters and propagation give you more control over what gets logged and where it goes.

### What is a Filter?
A filter lets you decide which log records are processed. For example, you might only want to log errors, not info messages.

### What is Propagation?
Propagation controls whether logs from a child logger are also sent to its parent logger. This helps you avoid duplicate logs or control log flow in big projects.

### Example: Filter
This filter only allows ERROR messages through:
```python
import logging

class OnlyErrors(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.ERROR

logger = logging.getLogger('filterDemo')
handler = logging.StreamHandler()
handler.addFilter(OnlyErrors())
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

logger.info('Info')    # Not printed
logger.error('Error')  # Printed
```

### Example: Propagation
This shows how to stop logs from bubbling up to parent loggers:
```python
import logging

parent = logging.getLogger('parent')
child = logging.getLogger('parent.child')

parent.setLevel(logging.INFO)
child.propagate = False

handler = logging.StreamHandler()
parent.addHandler(handler)
child.addHandler(handler)

child.info('Hello!')  # Printed only once, not propagated to parent
```

---
