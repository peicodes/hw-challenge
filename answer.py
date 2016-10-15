class CSVSnapshotParser(object):
    def __init__(self):
        self.snapshots = []

    def readFromFile(self, filename):
        del self.snapshots[:]
        try:
            file = open(filename, 'r')
            for line in file:
                tokens = line.split(',')
                if tokens[0] != "year":
                    daily = (float(tokens[0]), float(tokens[1]), float(tokens[2]))
                    self.snapshots.append(daily)
            return self.snapshots
        except:
            return None

class AnnualizedMWRCalculator(object):
    def __init__(self):
        self.functions = []
        self.functionPrimes = []

    def findAWR(self, x,n):
        for i in range(n):
            a = self.f(x)
            b = self.f_prime(x)
            if b == 0:
                return x
            x = x - a/b
        return x

    def f(self, x):
        sum = 0.0
        for function in self.functions:
            sum += function(x)
        return sum

    def f_prime(self, x):
        sum = 0.0
        for function in self.functionPrimes:
            sum += function(x)
        return sum

    def factory(self, cashValue, year):
        def annualizedAWR(x):
            return cashValue * (1 + x)**year
        return annualizedAWR

    def factoryPrime(self, cashValue, year):
        def annualizedAWR(x):
            return cashValue * (year - 1) (1 + x)**(year-1)
        return annualizedAWR


    def genFunctions(self, snapshots):
        numYears = len(snapshots) - 1
        for i in range(0, len(snapshots)):
            self.functions.append(self.factory(snapshots[i][1], numYears - snapshots[i][0]))
            self.functionPrimes.append(self.factory(snapshots[i][1], numYears - snapshots[i][0]))
        self.functions.append(self.factory(-1*snapshots[-1][1], 0))




parser = CSVSnapshotParser()
snapshots = parser.readFromFile(raw_input("File: "))
ans = AnnualizedMWRCalculator()
ans.genFunctions(snapshots)

print ans.findAWR(0, 100)
