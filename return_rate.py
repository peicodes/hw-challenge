import csv
with open('test.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    inputs = []
    year = -1
    for row in spamreader:
        inputs.append(row)
        year += 1

inputs = inputs[1:-1]
output = float(inputs[-1][2])

x = 0.2 # assume the return is 20% then if it's too large then x goes down or goes up
while True:
    y = 0
    for i in inputs:
        length = year - int(i[0])
        cash = float(i[1])
        value = float(i[2])
        y += cash*(1+x)**(year)
    if abs(y - output) > 10: # 10$ for estamate
        if y > output:
            x -= 0.001
        else:
            x += 0.001
    else:
        # print x, output, y
        break
print x
