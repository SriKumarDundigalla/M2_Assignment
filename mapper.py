import sys

for line in sys.stdin:
   
    line = line.strip()

    values = [int(val) for val in line.split()]
  
    total = sum(values)

    count = len(values)

    print(f'{count}\t{total}')

