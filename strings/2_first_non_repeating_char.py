#Brute Force Approach
#O(n2) - Time Complexity
#O(1) - Space Complexity
def firstNonRepeatingCharacter(string):
	for i in range(len(string)):
		foundDuplicate = False
		for j in range(len(string)):
			if string[i] == string[j] and j!=i:
				foundDuplicate = True
		if not foundDuplicate:
			return i
		
    return -1


#O(n) time | O(1) space - where n is the length of the input string
def firstNonRepeatingCharacter(string):
	letters = {}
	for letter in string:
		if letter in letters:
			letters[letter] +=1
		else:
			letters[letter] = 1
	for idx in range(len(string)):
		letter = string[idx]
		if letters[letter] == 1:
			return idx
		
	return -1
#humpy
