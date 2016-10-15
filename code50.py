import sys
import math
def sortIt(N):
	sorted = []
	first = True
	for chara in N:
		val = ord(chara)
		if first:
			sorted.append(val)
			first = False
			continue

		if val < sorted[-1]:
			sorted.append(val)
		elif val >= sorted[0]:
			sorted = [val] + sorted
		else:
			sorted.append(val)
	
	charL = []
	for x in sorted:
		charL.append(chr(x))
	return ''.join(charL)

def findIt(A):
    B = A[1:]
    C = []
    for item in B:
        C.append((item.strip("\n")).split(","))

    sum = 0
    cashFlowSum = 0
    first = True
    last = []
    for item in C:
        if first:
            first = False
            last = item
            continue
        print "%.2f" % ((pow((float(item[2])/(int(item[1])+float(last[2]))),(1/float(item[0])))-1)*100)
        last = item

    sys.exit()

results = []
firstLine = True
with open("test.csv") as f:
	contents = f.readlines()
findIt(contents)

file = open("a.out", "w")
counter = 1
for item in results:
	file.write("Case #" + str(counter) + ": " + item + "\n")
	counter += 1

file.close()