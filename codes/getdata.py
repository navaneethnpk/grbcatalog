import pandas as pd 
import re

grblist = ['https://gcn.nasa.gov/circulars/33635/raw',
 'https://gcn.nasa.gov/circulars/33580/raw',
 'https://gcn.nasa.gov/circulars/33579/raw',
 'https://gcn.nasa.gov/circulars/33578/raw',
 'https://gcn.nasa.gov/circulars/33577/raw',
 'https://gcn.nasa.gov/circulars/33569/raw',
 'https://gcn.nasa.gov/circulars/33558/raw',
 'https://gcn.nasa.gov/circulars/33551/raw',
 'https://gcn.nasa.gov/circulars/33485/raw',
 'https://gcn.nasa.gov/circulars/33478/raw',
 'https://gcn.nasa.gov/circulars/33475/raw',
 'https://gcn.nasa.gov/circulars/33472/raw',
 'https://gcn.nasa.gov/circulars/33471/raw',
 'https://gcn.nasa.gov/circulars/33466/raw',
 'https://gcn.nasa.gov/circulars/33465/raw',
 'https://gcn.nasa.gov/circulars/33461/raw',
 'https://gcn.nasa.gov/circulars/33459/raw',
 'https://gcn.nasa.gov/circulars/33449/raw',
 'https://gcn.nasa.gov/circulars/33448/raw',
 'https://gcn.nasa.gov/circulars/33447/raw',
 'https://gcn.nasa.gov/circulars/33444/raw',
 'https://gcn.nasa.gov/circulars/33443/raw',
 'https://gcn.nasa.gov/circulars/33442/raw',
 'https://gcn.nasa.gov/circulars/33439/raw',
 'https://gcn.nasa.gov/circulars/33438/raw',
 'https://gcn.nasa.gov/circulars/33437/raw',
 'https://gcn.nasa.gov/circulars/33434/raw',
 'https://gcn.nasa.gov/circulars/33431/raw',
 'https://gcn.nasa.gov/circulars/33430/raw',
 'https://gcn.nasa.gov/circulars/33429/raw',
 'https://gcn.nasa.gov/circulars/33428/raw',
 'https://gcn.nasa.gov/circulars/33427/raw',
 'https://gcn.nasa.gov/circulars/33425/raw',
 'https://gcn.nasa.gov/circulars/33424/raw',
 'https://gcn.nasa.gov/circulars/33419/raw',
 'https://gcn.nasa.gov/circulars/33418/raw',
 'https://gcn.nasa.gov/circulars/33416/raw',
 'https://gcn.nasa.gov/circulars/33415/raw',
 'https://gcn.nasa.gov/circulars/33414/raw',
 'https://gcn.nasa.gov/circulars/33413/raw',
 'https://gcn.nasa.gov/circulars/33412/raw',
 'https://gcn.nasa.gov/circulars/33411/raw',
 'https://gcn.nasa.gov/circulars/33410/raw',
 'https://gcn.nasa.gov/circulars/33407/raw',
 'https://gcn.nasa.gov/circulars/33406/raw',
 'https://gcn.nasa.gov/circulars/33405/raw']


# print(grblist)
for i in range(len(grblist)):
	number = re.findall(r'\d+',grblist[i])
	print(number[0])























