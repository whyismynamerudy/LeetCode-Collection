# link: https://leetcode.com/problems/reverse-integer/

"""

Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

"""

def reverse(self, x: int) -> int:
	negative = False
	if (x<0):
		x = abs(x)
		negative = True
	list1 = list(str(x))
	list2 = []
	for i in range(len(list1)):
		list2.inset(0, int(list[i]))
	strings = [str[inte] for inte in list2]
	aString = ''.join(strings)
	if (negative):
		aString = "-"+aString
	if (int(aString) >= -2147483647 and int(aString) <= 2147483646):
		return(int(aString))
	else:
		return 0