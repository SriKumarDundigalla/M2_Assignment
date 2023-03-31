#!/usr/bin/env python
import sys

total_sum = 0
count = 0
for line in sys.stdin:
    sum_str, count_str = line.strip().split()
    total_sum += int(sum_str)
    count += int(count_str)

print 'Average: %s' % (total_sum/count)