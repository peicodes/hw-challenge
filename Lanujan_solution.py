import csv

def interest(year0, year1, year1add):

	return ((((year1 - year1add)) / year0) - 1)

if __name__ == "__main__":
	list1 = []
	year0 = 0
	year1 = 0
	year1add = 0

	with open("test.csv") as csvfile:
		spamreader = csv.reader(csvfile)

		for row in spamreader:
			if row[0] == "year":
				pass
			else:
				list1.append(row)

		for i in list1:
			if i[0] == "0":
				year0 = float(i[2])

			if i[0] == "1":
				year1 = float(i[2])
				year1add = float(i[1])

		print interest(year0, year1, year1add)
