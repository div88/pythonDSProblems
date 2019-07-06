# Max and Min in a Unsorted Array
# In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

# Bonus Challenge: Is it possible to find the max and min in a single traversal?

import random

def get_min_max(ints):
	"""
	Return a tuple(min, max) out of list of unsorted integers.

	Args:
	   ints(list): list of integers containing one or more integers
	"""
	# print(ints)
	if(len(ints) == 0):
		tup="list is empty"
		return tup

	min = ints[0]
	max = ints[0]

	for i in range(1, len(ints)):
		if min > ints[i]:
			min = ints[i]

		if max < ints[i]:
			max = ints[i]
		tup = (min, max)
		
	print(tup)
	return tup
	

## Example Test Case of Ten Integers
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")


## Example Test Case 2
l = [i for i in range(2, 198)]  # a list containing 2 - 198
random.shuffle(l)

print ("Pass" if ((2, 197) == get_min_max(l)) else "Fail")

## Example Test Case 2
l = []  # empty list
random.shuffle(l)

print ("Pass" if ("list is empty" == get_min_max(l)) else "Fail")


