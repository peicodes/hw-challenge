file = open('test.csv', 'r')
file.readline()
snapshots = []
numThings = 8
for i in range(0,8):
        snapshots.append(file.readline()[0:-1].split(','))
final = 0
xEst = 0.5
def findEnd(tFinal):
        #initial cash flow
        tFinal = float(snapshots[0][1])
        #print "FISRT FINAL, ", final
        for j in range(1,len(snapshots)):
                tFinal += float(snapshots[j][1])*((1+xEst)**(numThings-j))
                #print "nfinal: ", final
        return tFinal
final = findEnd(final)
loops = 1
while abs(final-float(snapshots[-1][2]))>0.001:
        #print "Final: ", final, "Real: ", snapshots[-1][2]
        if final < float(snapshots[-1][2]):
                xEst -= 0.000001
        else:
                xEst += 0.000001
        final = findEnd(final)
print xEst

