"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		seen_chars = []
		count = 0
		max_count = 0

		for char in s:
			if char not in seen_chars:
				seen_chars.append(char)
				count += 1
				if count > max_count:
					max_count = count

				continue

			count = 0
			seen_chars = []

		return max_count

class Solution2:
	def lengthOfLongestSubstring(self, s: str) -> int:
		char_set = set()
		res, l = 0, 0

		for i in range(len(s)):
			while s[i] in char_set:
				char_set.remove(s[l])
				l += 1
			char_set.add(s[i])
			res = max(res, i - l + 1)
		return res



if __name__ == '__main__':
	S = Solution2()

	print('abcabcbb -> 3: ', S.lengthOfLongestSubstring('abcabcbb'))
	print('bbbbb -> 1: ', S.lengthOfLongestSubstring('bbbbb'))
	print('pwwkew -> 3: ', S.lengthOfLongestSubstring('pwwkew'))
	print('a -> 1: ', S.lengthOfLongestSubstring('a'))
	print('" " -> 1: ', S.lengthOfLongestSubstring(' '))
