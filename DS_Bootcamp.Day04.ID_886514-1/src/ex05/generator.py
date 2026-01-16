#!/usr/bin/env python3

import sys
import resource

def read_file_generator(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generator.py <path_to_ratings.csv>")
        sys.exit(1)

    file_path = sys.argv[1]
    line_generator = read_file_generator(file_path)

    for line in line_generator:
        pass

    peak_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024*1024)
    print(f"Peak Memory Usage = {peak_memory:.3f} GB")

    user_time = resource.getrusage(resource.RUSAGE_SELF).ru_utime
    system_time = resource.getrusage(resource.RUSAGE_SELF).ru_stime
    total_time = user_time + system_time
    print(f"User Mode Time + System Mode Time = {total_time:.2f}s")
