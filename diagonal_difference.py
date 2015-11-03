'''




'''
import sys 
data = []
for line in sys.stdin:
	data.append(line)

# print(data)
matrix = [map(int, pozycja.split()) for pozycja in data]
size = map(int, matrix[0])
n = size[0]
matrix = matrix[1:]
# print(size)
# print(matrix)
diag1 = diag2 = 0
for i in range(n):
	diag1 += matrix[i][i]
	diag2 += matrix[i][-1-i]
print(abs(diag1-diag2))
