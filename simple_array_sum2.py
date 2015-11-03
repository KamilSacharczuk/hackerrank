import sys 
data = [] 
for line in sys.stdin:
	data.append(line) 
n = int(data[0]) 
string = data[1] 
print(sum(map(int, string.split())))
