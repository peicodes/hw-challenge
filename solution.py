f = open("test.csv", "r")

ls = f.read().splitlines()
final = ls[8].split(",")[2]

sum = 0
flows = 0

for i in ls[1:-1]:
    total = i.split(",")[2]
    cash = i.split(",")[1]
    if "." in cash:
        cash = cash[:-3]
    flows += int(cash)
    yr = i.split(",")[0]
    w = (7 - int(yr))/7
    sum += w * int(cash)

result = (float(final) - float(flows))/sum

print(result)