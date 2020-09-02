# Given a column title as appear in an Excell sheed, return its corresponding column number

# For Example:
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28

# Constraints
# 1 <= s.length <= 7
# s consists only of uppercase English letters.
# s is between "A" and "FXSHRXW".

# ------------------------------------------------------------------
from math import pow

class Solution:
	def titleToNumber(self, s: str) -> int:
		column = 0
		length = len(s)
		for i in range(length):
			column += (ord(s[i]) - 64) * pow(26, length - i - 1)

		return round(column)



if __name__ == '__main__':
	S = Solution()
	print('A -> 1: ', S.titleToNumber('A'))
	print('B -> 2: ', S.titleToNumber('B'))
	print('C -> 3: ', S.titleToNumber('C'))
	print('Z -> 26: ', S.titleToNumber('Z'))
	print('AA -> 27: ', S.titleToNumber('AA'))
	print('AZ -> 52: ', S.titleToNumber('AZ'))
	print('BA -> 53: ', S.titleToNumber('BA'))
	print('AB -> 28: ', S.titleToNumber('AB'))
	print('AAB -> 704: ', S.titleToNumber('AAB'))
	print('ASFG -> 30583: ', S.titleToNumber('ASFG'))
	print('FXSHRXW -> 2147483647: ', S.titleToNumber('FXSHRXW'))
