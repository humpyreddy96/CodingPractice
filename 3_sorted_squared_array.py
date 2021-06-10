#Approach 1
#Straight forward.
#O(nlogn)
def sortedSquaredArray(array):
    nums = []
    for num in array:
        nums.append(num*num)
    nums.sort()
    return nums

def sortedSquaredArray1(array):
    nums = []


nums = sortedSquaredArray([-2,1])

#Approach 2
#To reduce the time complexity for linear time complexity
#Compares the start Index absolute value and the end index absolute value, squares it and fills the array from the end

array = [-7,-5,-4,3,6,8,9]

def sortedSquares(array):
    sortedSquares = [0 for _ in array]
    startIndex = 0
    endIndex = len(array)-1
    i = len(array)-1

    while(startIndex<=endIndex):
        if abs(array[startIndex])<(array[endIndex]):
            value = array[endIndex]
            sortedSquares[i] = value*value
            endIndex -=1
        else:
            value = array[startIndex]
            sortedSquares[i]=value*value
            startIndex +=1
        i -=1
    return sortedSquares

print(sortedSquares(array))


