coins = [5,7,1,1,2,3,22]

def nonConstructibleChange(coins):
    coins.sort()
    currentChange = 0
    for coin in coins:
        if coin>currentChange+1:
            return currentChange+1
        currentChange +1= coin
    return currentChange+1
    

