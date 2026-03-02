# MultiProcessing for CPU bound tasks
# Factorial calculations especially for large numbers, involve significant computational work.
# Multiprocessing can be used to distribute the workload across multiple CPU cores to improve performance

import multiprocessing
import math
import sys
import time


# Increase maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

# Function to compute factorial of a given number
def compute_factorial(number):
    print(f"Computing factorial of {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__ == "__main__":
    numbers = [5000,6000,7000,8000]

    start_time = time.time()

    # Creating a pool of worker processes
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial,numbers)

    end_time = time.time()

    print(f"The results are : {results}")
    print(f"The computation took around {end_time - start_time}") # Took around 0.52 seconds
