import sys
total = 0
count = 0
for line in sys.stdin:
    line = line.strip()
    val_count, val_total = line.split('\t', 1)
    try:
        val_count = int(val_count)
        val_total = int(val_total)
    except ValueError:

        continue
    total += val_total
    count += val_count
if count > 0:
    avg = total / count
    print '%s' % (avg)
else:
    print('No data')
