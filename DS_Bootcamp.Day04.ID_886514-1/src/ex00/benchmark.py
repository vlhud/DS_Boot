#!/usr/bin/env python3

import timeit

emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']

def usual_approach(em):
    email_list=[]
    for email in em:
        if email.endswith('@gmail.com'):
            email_list.append(email)
    return email_list

def list_comprehension(em):
    return [email for email in em if email.endswith('@gmail.com')]

if __name__ == '__main__':
    emails_list = emails * 5
    usual_time = timeit.timeit('usual_approach(emails_list)', globals=globals(), number=90000000)

    comprehension_time = timeit.timeit('list_comprehension(emails_list)', globals=globals(), number=90000000)
    if comprehension_time <= usual_time:
        print("it is better to use a list comprehension")
    else:
        print("it is better to use a loop")

    shortest_time = min(usual_time, comprehension_time)
    longest_time = max(usual_time, comprehension_time)
    print(f"{shortest_time} vs {longest_time}")