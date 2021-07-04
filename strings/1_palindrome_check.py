def isPalindrome(string):
	
	reversedString = ""
	for i in reversed(range(len(string))):
		reversedString +=string[i]
	
	return reversedString == string