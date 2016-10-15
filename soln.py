import csv 

with open('test.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',', quotechar='|')
    x = 0.1;
    value_list = list(reader)[1:]
    market_value = float(value_list[-1][2])
    temp = 0;
    while 1:
        for i in range(len(value_list) - 1):
            temp += float(value_list[i][2]) * pow((1 + x), i);
        
        if round(temp - market_value, 2) < 0.005:
            break

        if round(temp, 2) - market_value > 0.001:
            x -= 0.00001;
            temp = 0
        elif round(temp, 2) - market_value < 0.001:
            x += 0.00001;
            temp = 0
        else:
            break

    print x;
        
    

# snapshot[0].cash_flow * (1 + x) ^ (n - 1) + snapshot[1].cash_flow * (1 + x) ^ (n - 2) + ... + snapshot[n-2].cash_flow * (1 + x) ^ 1 = snapshot[n-1].market_value
        
