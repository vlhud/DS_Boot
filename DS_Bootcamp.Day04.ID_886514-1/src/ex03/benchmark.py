#!/usr/bin/env python3

import timeit
import sys
from functools import reduce

def sum_of_squares_loop(n):
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total

def sum_of_squares_reduce(n):
    return reduce(lambda acc, x: acc + x * x, range(1, n + 1), 0)

def benchmark(method_name, num_calls, n):
    methods = {
        'loop': sum_of_squares_loop,
        'reduce': sum_of_squares_reduce
    }

    if method_name not in methods:
        print(f"Invalid method name: {method_name}. Choose from {list(methods.keys())}.")
        return

    time_taken = timeit.timeit(lambda: methods[method_name](n), number=num_calls)
    print(time_taken)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python benchmark.py <method> <number_of_calls> <n>")
        sys.exit(1)

    method = sys.argv[1]
    try:
        calls = int(sys.argv[2])
        n = int(sys.argv[3])
    except ValueError:
        print("Please provide valid integers for the number of calls and n.")
        sys.exit(1)

    benchmark(method, calls, n)