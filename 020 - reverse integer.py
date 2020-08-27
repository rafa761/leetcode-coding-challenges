"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer
 range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when
  the reversed integer overflows.
"""


class Solution:
	def reverse(self, x):
		s = (x > 0) - (x < 0)
		r = int(str(x * s)[::-1])
		return s * r * (r < 2 ** 31)


if __name__ == '__main__':
	S = Solution()

	print('321 -> ', S.reverse(123))
	print('-12 -> ', S.reverse(-21))
	print('0 -> ', S.reverse(219879797987897987987897987897987897899879879879879879879879))
