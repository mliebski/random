#!python3

import sys, math, datetime, time

#from numba import jit

#jit

counter = 0
init_value = sys.argv[1]
print("Start Value: " + init_value)
step_count = 0
#check for even or odd

calc_value = float(init_value)

while calc_value !=1:
	if calc_value % 2 == 0:
		calc_value = calc_value/2
	else:
		calc_value = 3*calc_value +1
	step_count = step_count + 1
	print("Zwischenergebnis: " + str(calc_value))



start = time.time()
print("start is {:%H:%M:%S}".format(datetime.datetime.now()))
print("Finish is {:%H:%M:%S}".format(datetime.datetime.now()))
print("Endergebnis ist: " + str(calc_value))
print("Schrittzahl: " + str(step_count))
finish = time.time()
duration = finish - start
print("Duration was: " + str(duration))
