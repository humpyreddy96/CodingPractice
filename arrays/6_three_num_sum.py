array = [12,3,1,2,-6,5,-8,6]
targetSum = 0

#return a list of triplets which equals the target sum

def threeNumSum(array,targetSum):
    
    array.sort()
    triplets=[]
    for i in range(len(array)-1):
        leftIndex = i+1
        rightIndex = len(array)-1

        while leftIndex<rightIndex:
            currentSum = array[i]+array[leftIndex]+array[rightIndex]

            if currentSum<targetSum:
                leftIndex +=1
            elif currentSum>targetSum:
                rightIndex -=1
            elif currentSum == targetSum:
                triplets.append([array[i],array[leftIndex],array[rightIndex]])
                leftIndex +1
                rightIndex -=1
    return triplets

print(threeNumSum(array,targetSum))

