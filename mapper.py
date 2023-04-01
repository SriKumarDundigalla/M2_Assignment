#!/usr/bin/env python
"""mapper.py"""
import sys

for line in sys.stdin:
    sum_numbers=0
    count=0
    line = line.strip()

    numbers=line.split()

    for num in numbers:
        sum_numbers = int(num)+sum_numbers
        count = count+1

    print '%s\t%s' % (count,sum_numbers)

