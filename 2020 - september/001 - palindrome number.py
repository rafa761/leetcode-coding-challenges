"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:
Coud you solve it without converting the integer to a string?
"""


class Solution:
	def isPalindrome(self, x: int) -> bool:
		return str(x) == str(x)[::-1]


class Solution2:
	def isPalindrome(self, x: int) -> bool:
		return x == self.reverse(x)

	def reverse(self, n, rev=0):
		# Base case
		if n <= 0:
			return rev

		rev = rev * 10 + (n % 10)
		rev = self.reverse(n // 10, rev)
		return rev


if __name__ == '__main__':
	S = Solution2()

	print('true -> ', S.isPalindrome(121))
	print('false -> ', S.isPalindrome(-121))
	print('false -> ', S.isPalindrome(10))
