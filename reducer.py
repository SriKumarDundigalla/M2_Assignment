#!/usr/bin/env python
"""reducer.py"""

# Import the sys module to read input from standard input
import sys

# Initialize the variables to hold the total and count
total = 0
count_tot = 0

# Loop through each line of input from standard input
for line in sys.stdin:

    # Strip any whitespace or newline characters from the line
    line = line.strip()

    # Split the line into the key and value based on the tab separator
    num, count = line.split('\t', 1)

    # Try to convert the key and value to integers
    try:
        num = int(num)
        count = int(count)
    # If either value cannot be converted to an integer, skip to the next line
    except ValueError:
        continue

    # Increment the total by the current key value and the count by the current value
    total = num + total
    count_tot = count + count_tot

# If the count is greater than 0, print the average
if count > 0:
    print 'avg:%s' % (total / float(count_tot))
