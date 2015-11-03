'''


Problem Statement

You are given an array of integers of size N. Can you find the sum of the elements in the array?

Input
The first line of input consists of an integer N. The next line contains N space-separated integers representing the array elements.
Sample:

6

1 2 3 4 10 11

Output
Output a single value equal to the sum of the elements in the array.
For the sample above you would just print 31 since 1+2+3+4+10+11=31.

'''
import sys 
data = [] 
for line in sys.stdin:
	data.append(line) 
n = int(data[0]) 
string = data[1] 
liczby = [int(pozycja) for pozycja in string.split() ] 
print(sum(liczby)) 
