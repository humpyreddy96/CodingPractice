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
#using space efficiently



