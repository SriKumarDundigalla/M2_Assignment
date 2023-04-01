#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

total = 0
count = 0

for line in sys.stdin:


    val_count, val_total = line.split('\t', 1)


    try:
        val_count = int(val_count)
        val_total = int(val_total)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    total += val_total
    count += val_count
if count > 0:
    avg = total / count
    print 'Average: %s' % (total_sum/count)



