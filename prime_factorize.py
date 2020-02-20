#!python3

import sys, math, datetime, time

from numba import jit

jit
def factorize(n):
	factors = []
	i = 2
	while n>1:
#		print(n)
		if n%i == 0:
			n = n/i
			factors.append(i)
			print(i)
		else:
			i +=1
	return factors

jit
def condense(L):
	prime, count, list = 0,0,[]
	for x in L:
		if x == prime:
			count = count + 1
		else:
			if prime !=0:
				list = list + [str(prime) + '^' + str(count)]
			prime, count = x,1
	list = list + [str(prime) + '^' + str(count)]
	return list

start = time.time()
print("start is {:%H:%M:%S}".format(datetime.datetime.now()))

print (condense(factorize(int(sys.argv[1]))))
print("Finish is {:%H:%M:%S}".format(datetime.datetime.now()))
finish = time.time()
duration = finish - start
print("Duration was: " + str(duration))
	
