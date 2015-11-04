import sys
	
tests = int(input())
for i in range(1,tests+1):
	[n, k] = map(int, sys.stdin.readline().split())
	students = map(int, sys.stdin.readline().split())
	if len([s for s in students if s<=0]) < k:
		print "YES"
	else:
		print "NO"
