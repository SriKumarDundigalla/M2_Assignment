#!/usr/bin/env python
import sys

for line in sys.stdin:
    values = line.strip().split()
    total_sum = 0
    count = 0
    for val in values:
        total_sum += int(val)
        count += 1
    print '%s\t%s' % (total_sum, count)