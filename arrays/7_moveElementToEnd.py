def moveElementToEnd(array, toMove):
    # Write your code here.
	startIndex = 0
	endIndex = len(array)-1
	
	while startIndex<endIndex:
		if array[endIndex]==toMove:
			endIndex -=1
		elif array[startIndex]==toMove:
			swap(array,startIndex,endIndex)
			startIndex +=1
			endIndex -=1
		else:
			startIndex +=1
			
	return array
			

def swap(array,startIndex,endIndex):
	temp = array[endIndex]
	array[endIndex] = array[startIndex]
	array[startIndex] = temp
			