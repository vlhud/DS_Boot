#!/usr/bin/env python3

import timeit
import sys

emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']*5

def usual_approach(em):
    email_list=[]
    for email in em:
        if email.endswith('@gmail.com'):
            email_list.append(email)
    return email_list

def list_comprehension(em):
    return [email for email in em if email.endswith('@gmail.com')]

def map_approach(em):
    return list(map(lambda x: x if x.endswith('@gmail.com') else None, em))

def filter_approach(em):
    return list(filter((lambda email: email.endswith('@gmail.com')), em))

def benchmark(method_name, num_calls):
    
    methods = {
        'loop': usual_approach,
        'list_comprehension': list_comprehension,
        'map': map_approach,
        'filter': filter_approach
    }

    if method_name not in methods:
        print(f"Invalid method name: {method_name}. Choose from {list(methods.keys())}.")
        return

    time_taken = timeit.timeit(lambda: methods[method_name](emails), number=num_calls)
    print(time_taken)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python benchmark.py <method> <number_of_calls>")
        sys.exit(1)

    method = sys.argv[1]
    try:
        calls = int(sys.argv[2])
    except ValueError:
        print("Please provide a valid integer for the number of calls.")
        sys.exit(1)

    benchmark(method, calls)