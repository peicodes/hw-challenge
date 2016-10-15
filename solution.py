#!/usr/bin/python

from operator import mul

with open("test.csv") as raw:
	raw.next()
	data = [[float(p) for p in line.rstrip("\n").split(",")] for line in raw]
	n = len(data)
	
	data, final = [x for x in data if x[1] != 0], data[-1][2]

	# print data, final
	print (final/reduce(mul, [x[1] for x in data]))**(1/(sum([n-x[0] for x in data])))/10