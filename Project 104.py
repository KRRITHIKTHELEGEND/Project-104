import csv

with open('SOCR-HeightWeight.csv', newline='') as ok:
	something = csv.reader(ok)
	data = list(something)

	data.pop(0)
	heightData = []
	weightData = []
	for i in range(len(data)):
		heightThing = data[i][1]
		weightThing = data[i][2]
		heightData.append(float(heightThing))
		weightData.append(float(weightThing))
	heightLength = len(heightData)
	weightLength = len(weightData)

def mean():

	heightTotal = 0
	weightTotal = 0
	for x in heightData:
		heightTotal += x
	for x in weightData:
		weightTotal += x

	heightMean = heightTotal/heightLength
	weightMean = weightTotal/weightLength

	print("\n-------------------\n\nThe Mean Of The Height Is ", heightMean, "\nThe Mean Of The Weight Is ", weightMean)

def median():

	heightData.sort()
	weightData.sort()

	if(heightLength % 2 == 0):
		heightMedian1 = float(heightData[heightLength//2])
		heightMedian2 = float(heightData[heightLength//2 - 1])
		heightMedian = (heightMedian1 + heightMedian2)/2
	else:
		heightMedian = heightData[heightLength//2]

	if(weightLength % 2 == 0):
		weightMedian1 = float(weightData[weightLength//2])
		weightMedian2 = float(weightData[weightLength//2 - 1])
		weightMedian = (weightMedian1 + weightMedian2)/2
	else:
		weightMedian = weightData[weightLength//2]

	print("\n-------------------\n\nThe Median Of The Height Is ", heightMedian, "\nThe Median Of The Weight Is ", weightMedian)

def main():

	mean()
	median()

main()