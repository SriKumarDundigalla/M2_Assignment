import sys
sum_numbers=0
count=0
for line in sys.stdin:
   
    line = line.strip()

    numbers=line.split()

    for num in numbers:
        sum_numbers = int(num)+num
        count = count+1

    print '%s\t%s' % (count,sum_numbers)

