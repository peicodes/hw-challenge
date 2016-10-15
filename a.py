import csv
with open('test.csv', 'rb') as f:
    reader = csv.reader(f)
    val=[]
    val1=[]
    i=0
    for a in reader:
        val.append(a[1])
        val1.append(a[2])

    ab=float(val1[2])
    bc=float(val1[1])
    d=ab-bc-float(val[2])
    v=d/bc
    print v
    
    
