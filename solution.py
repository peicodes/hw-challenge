def derivative(x):  # Derivative function of polynomial
    ans = 0
    for i in range(n):
        degree = n - i - 1
        ans += degree * cash_flow[i] * x ** (degree - 1)
    return ans


def f(x):  # Polynomial
    ans = 0
    for i in range(n):
        degree = n - i - 1
        ans += cash_flow[i] * x ** degree
    ans -= market_value[-1]  # Last market value
    return ans


def solution():
    current = 1.5
    x = 500  # Adjust to higher value for more precision
    for i in range(x):
        current = current - (f(current) / derivative(current))
    return current - 1


data = open("test2.csv").readlines()
cash_flow = []
market_value = []
for line in data[1:]:
    a, b, c = [float(i) for i in line.split(",")]
    cash_flow.append(b)
    market_value.append(c)
n = len(cash_flow)
print(solution())
