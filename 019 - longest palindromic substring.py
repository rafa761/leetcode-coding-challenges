"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
"""


class Solution:
	def longestPalindrome(self, s: str) -> str:
		max_palindrome = ''
		for i in range(len(s)):
			for j in range(len(s), i, -1):
				if len(max_palindrome) >= j - i:
					break

				elif s[i:j] == s[i:j][::-1]:
					max_palindrome = s[i:j]
					break

		return max_palindrome


class Solution2:
	def longestPalindrome(self, s: str) -> str:
		res = ''
		for i in range(len(s)):
			res = max(self.helper(s, i, i), self.helper(s, i, i + 1), res, key=len)

		return res

	def helper(self, string, left, right):
		while left >= 0 and right < len(string) and string[left] == string[right]:
			left -= 1
			right += 1
		return string[left + 1:right]


if __name__ == '__main__':
	S = Solution2()

	print('bab -> ', S.longestPalindrome('babad'))
	print('bb -> ', S.longestPalindrome('cbbd'))
	print('bb -> ', S.longestPalindrome('abb'))
