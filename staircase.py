import sys
n = int(input())
for i in range(1,n+1):
	#print("%s%s" % (' ' * (n-i),'#' * i))
	print " "*(n-i)+"#"*i
