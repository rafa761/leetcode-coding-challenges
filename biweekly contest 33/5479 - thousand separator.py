"""
5479. Thousand Separator

Given an integer n, add a dot (".") as the thousands separator and return it in string format.


Example 1:
Input: n = 987
Output: "987"

Example 2:
Input: n = 1234
Output: "1.234"

Example 3:
Input: n = 123456789
Output: "123.456.789"

Example 4:
Input: n = 0
Output: "0"
"""


class Solution:
	def thousandSeparator(self, n: int) -> str:
		return f"{n:,}".replace(',', '.')


if __name__ == '__main__':
	S = Solution()

	print('943 -> ', S.thousandSeparator(943))
	print('1.234 -> ', S.thousandSeparator(1234))
	print('123.456.789 -> ', S.thousandSeparator(123456789))
