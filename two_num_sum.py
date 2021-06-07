
array = [3,5,-4,8,11,1,-1,-6]
targetSum = 10

#Approach 1
#Store the first number in one variable, iterate throught out the rest of the array to see if the sum of the 
#first num and second number equals the target sum.

def twoNumSum1(array,targetSum):
    for i in range(len(array)-1):
        firstNum = array[i]
        for j in range(i+1,len(array)):
            secondNum = array[j]
            if(firstNum+secondNum==targetSum):
                return [firstNum,secondNum]
    return []

#Approach 2
#sort the array
#have two pointers one at the first index, other at the end of the array.
#if the sum of the first and the last index is greater than the target sum, the right pointer moves to the left
#if the sum of the first and the last index is less than the target sum, the left pointer moves to the right.
#this repeats till the target sum is achieved else returns an empty array.

def twoNumSum2(array,targetSum):
    array.sort()
    leftIndex = 0
    rightIndex = len(array)-1
    
    while(leftIndex<rightIndex):
        if array[leftIndex]+array[rightIndex]>targetSum:
            rightIndex = rightIndex-1
        elif array[leftIndex]+array[rightIndex]<targetSum:
            leftIndex = leftIndex+1
        elif array[leftIndex]+array[rightIndex]==targetSum:
            return [array[leftIndex],array[rightIndex]]
    

    return []

#Approach 3
#The difference approach, it takes the difference of target and one number and checks the array if the difference 
#exists. If it does it returns those two numbers, else returns an empty array.

def twoNumSum3(array,targetSum):
    nums = []
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [num,potentialMatch]
        else:
            nums[num]=True
    return []
    
print(twoNumSum1(array,targetSum))
print(twoNumSum2(array,targetSum))
print(twoNumSum3(array,targetSum))


