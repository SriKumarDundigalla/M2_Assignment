#!/usr/bin/env python
"""mapper.py"""

# Import the sys module to read input from standard input
import sys

# Loop through each line of input from standard input
for line in sys.stdin:

    # Strip any whitespace or newline characters from the line
    line = line.strip()

    # Split the line into a list of numbers based on whitespace as the delimiter
    numbers = line.split()

    # Loop through each number in the list and output a key-value pair
    # consisting of the number and a count of 1
    for num in numbers:
        print '%s\t%s' % (num, 1)

