def buzzCheck(checkMe, divisibleBy, displayMe):
	"""Checks if a given number is divisible by another. 
	It fit is, a section of text is added to the variable.

	checkMe (int)     - The number to check
	divisibleBy (int) - What to check that 'chackMe' is divisible by
	displayMe (str)   - WWhat to display if 'checkMe' is divisible by 'divisibleBy'

	Exmple Input: buzzCheck(2, 3, "Fizz")
	Exmple Input: buzzCheck(5, 5, "Buzz")
	Exmple Input: buzzCheck(15, 3, "Fizz")
	"""
	global output

	if (not bool(checkMe % divisibleBy)):
		output += displayMe

def fizzBuzz(leftBound = 1, rightBound = 100):
	"""Outputs a list of numbers on a new line from a left and right bound.
	Any number that is a multiple of 3 is replaced with "Fizz", and
	any number that is a multiple of 5 is replaced with "Buzz".
	If it is a multiple of both 3 and 5, it will be replaced with "FizzBuzz".

	leftBound (int)  - What number to start at
	rightBound (int) - What number to end at

	Example Input: fizzBuzz()
	Example Input: fizzBuzz(50, 100)
	Example Input: fizzBuzz(rightBound = 200)
	"""
	global output

	for i in range(leftBound, rightBound + 1):
		output = ""
		buzzCheck(i, 3, "Fizz")
		buzzCheck(i, 5, "Buzz")

		if (len(output) == 0):
			print(i)
		else:
			print(output)

fizzBuzz()