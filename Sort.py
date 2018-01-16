import pdb

def findMax(list):
	n = len(list)
	max = 0
	for i in list:
		if i > max:
			max = i
	return max

def findMin(list):
	n = len(list)
	min = list[0]
	for i in list:
		if i < min:
			min = i
	return min

def bucketSort(list):
	pivot = (findMax(list) + findMin(list))/2
	n = len(list)
	greater = []
	lesser = []
	if n > 1:
		for i in list:
			if i < pivot:
				lesser.append(i)
			else:
				greater.append(i)
		list = bucketSort(lesser) + bucketSort(greater)
		return list
	else: 
		return list

def bubbleSort(list):
	for a in range(len(list)-1):
		for i in range(len(list) -1):
			if list[i] > list[i+1]:
				temp = list[i]
				list[i] = list[i+1]
				list[i+1] = temp
				print(list)

def selectionSort(list):
	for i in range(len(list)-1):
		minDex = i
		for x in range(len(list[i:])):
			if list[x+i] < list[minDex]:
				minDex = x + i
		#pdb.set_trace()		
		tempMin = list[minDex]
		temp = list[i]
		list[i] = tempMin
		list[minDex] = temp
		print(list)