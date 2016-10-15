import csv



def poly_eval(x, coeffs):
    y = 0
    for n in xrange(len(coeffs)):
        y += coeffs[n]*(x**n)

    return y



with open('test.csv', 'rb') as f:
    reader = csv.reader(f)
    raw_data = [row for row in reader]

N = len(raw_data) - 1

poly_coeffs = list()
final_market_value = float(raw_data[-1][-1])
poly_coeffs.append(-1*final_market_value)
for i in xrange(N-1, 0, -1):
    poly_coeffs.append(float(raw_data[i][1]))
    

f = lambda x: poly_eval(x, poly_coeffs)

def bisect(a, b, f, tol):
    mid = 0.5*(a+b)

    if abs(b-a) < tol:
        return mid

    if f(a)*f(mid) < 0:
        return bisect(a, mid, f, tol)
    else:
        return bisect(mid, b, f, tol)

print bisect(1, 2, f, 1e-6) 


#from numpy import *
#from matplotlib import pyplot as plt
#
#t = arange(1, 1.1, 0.001)
#plt.plot(t, f(t))
#plt.show()


