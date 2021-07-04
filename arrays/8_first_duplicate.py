#Approach 1 - O(n2)
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

	#Approach 2 - O(n) - linear time
	#using sets

	def firstDuplicateValue(array):
    # Write your code here.
    seen = set()
	for value in array:
		if value in seen:
			return value
		else:
			seen.add(value)
	return -1
	 
	