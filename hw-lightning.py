def getMwr(allSnaps):
    '''
    Uses Newtons method for finding IRR/mwr #UW MATH represent
    It converges quadratically aka it's pretty fast :)

    I was gonna use brent's method but that's not as clear. 
    I decided to use Newton's since it's much clearer code wise
    '''
    numIterations=0
    maxIterations=400
    allowedError=0.0001 #10x the precision

    prevGuess=[1, 0] #prevGuess[0] = 2nd last guess, prevGuess[1] = last guess
    finalMarketValue=allSnaps[-1][2]
    numPeriods = len(allSnaps)

    while(abs(prevGuess[0] - prevGuess[1]) > allowedError):
        prevGuess[0] = prevGuess[1]
        derivRate = derivIrr(allSnaps, prevGuess[0], numPeriods)
        eir = (evalIrr(allSnaps, prevGuess[0], numPeriods)-finalMarketValue)
        #Will cause div zero error, and having a zero derivRate means you 
        #contribute nothing but gained market value (money from thin air?)
        if (derivRate == 0):
            return "undefined"
        prevGuess[1] = prevGuess[0] - eir / derivRate
        numIterations+=1
        #Too many iterations probably means non-convergence
        if (numIterations > maxIterations):
            return "undefined"
    return prevGuess[1]

def evalIrr(allSnaps, testIrr, numYears):
    retVal = 0 
    for year, cf, mv in allSnaps:
        retVal += cf*(1+testIrr)**(numYears-year-1)
    return retVal

def derivIrr(allSnaps, testIrr, numYears):
    retVal = 0
    for year, cf, mv in allSnaps:
        retVal += (numYears-year-1)*cf*(1+testIrr)**(numYears-year-2)
    return retVal

f = open('test.csv', 'r')

#Parsing
#convert input into nested list
allSnaps = []
for snapshot in f.read().split()[1:]: #ignore line 0 b/c it's not numbers 
    allSnaps.append([float(number) for number in snapshot.split(",")])

print(getMwr(allSnaps))
