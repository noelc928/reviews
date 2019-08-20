data = []
datalen = 0
datashort = []
datagood =[]
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		datalen += len(line)
		if len(line)<100:
			datashort.append(line)
		if 'good' in line:
			datagood.append(line)
print(len(data))
print(datalen/len(data))
print('小於100的留言', len(datashort))
print('提到good的留言', len(datagood))