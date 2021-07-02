def firstDuplicateValue(array):
    # Write your code here.
	index = len(array)
	for i in range(len(array)):
		num = array[i]
		for j in range(i+1,len(array)):
			if array[j] == num and index>j :
				index = j
	if index == len(array):
		return -1
	return array[index]