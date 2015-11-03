import sys

import sys 
data = []
for line in sys.stdin:
	data.append(line)

n = int(data[0])
array = [int(pozycje) for pozycje in data[1].split()]
# print(array)
plus = minus = zeros = 0
for i in array:
    if i>0:
        plus += 1
    elif i==0:
        zeros += 1
    else:
        minus += 1
print("%.4f" % (plus/n))
print("%.4f" % (minus/n))
print("%.4f" % (zeros/n))
