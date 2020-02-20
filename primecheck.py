#!python3
import sys
from math import sqrt
from numba import jit
@jit
def is_prime(x):
	prime = False
	if x > 1:
		prime = True
		k = 2
		n = sqrt(x) 
		while k <= n and prime == True:
			if x%k ==0:
				prime = False
			k += 1
	return prime

i = 1
pc = 0
test_range = int(sys.argv[1])
while i < test_range:
	num = i
	i = i + 1
	
	if is_prime(num):
		print (str(num) + "is a prime number")
		pc = pc +1
	else:
		print (str(num) + "is a composite number")

print (str(pc) + " prime numbers found in " + str(test_range))
