#!/usr/bin/env python3

import timeit
import random
from collections import Counter

random_values = [random.randint(0, 100) for _ in range(1_000_000)]

def count_values_manual(values):
    counts = {i: 0 for i in range(101)}
    for value in values:
        counts[value] += 1
    return counts

def top_ten_manual(values):
    counts = count_values_manual(values)
    return dict(sorted(counts.items(), key=lambda item: item[1], reverse=True)[:10])

def count_values_counter(values):
    return Counter(values)

def top_ten_counter(values):
    return dict(Counter(values).most_common(10))

if __name__ == "__main__":
    manual_count_time = timeit.timeit("count_values_manual(random_values)", globals=globals(), number=10)
    manual_top_time = timeit.timeit("top_ten_manual(random_values)", globals=globals(), number=10)

    counter_count_time = timeit.timeit("count_values_counter(random_values)", globals=globals(), number=10)
    counter_top_time = timeit.timeit("top_ten_counter(random_values)", globals=globals(), number=10)

    print(f"My function (count): {manual_count_time:.7f}")
    print(f"Counter (count): {counter_count_time:.7f}")
    print(f"My top (manual): {manual_top_time:.7f}")
    print(f"Counter's top: {counter_top_time:.7f}")
