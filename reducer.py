#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

total=0
count_tot=0

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    num,count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
	    num=int(num)
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    total=num+total
    count_tot=count+count_tot
if count >0:
   print 'avg:%s'%(total/float(count_tot))
