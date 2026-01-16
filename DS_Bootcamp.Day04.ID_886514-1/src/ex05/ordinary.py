#!/usr/bin/env python3

import sys
import resource

def read_file_to_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ordinary.py <path_to_ratings.csv>")
        sys.exit(1)

    file_path = sys.argv[1]
    lines = read_file_to_list(file_path)

    for line in lines:
        pass

    peak_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024*1024)
    print(f"Peak Memory Usage = {peak_memory:.3f} GB")

    user_time = resource.getrusage(resource.RUSAGE_SELF).ru_utime
    system_time = resource.getrusage(resource.RUSAGE_SELF).ru_stime
    total_time = user_time + system_time
    print(f"User Mode Time + System Mode Time = {total_time:.2f}s")
