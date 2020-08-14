"""
Given a s which consists of lowercase or uppercase letters, find the length of the longest palindromes
that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given s will not exceed 1,010.

Example:

Input: "abccccdd"
Output: 7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""
from collections import Counter


class Solution2:
	def longestPalindrome(self, s: str) -> int:
		letters_dict = Counter(s)
		res = odd = 0
		for value in letters_dict.values():
			if value % 2 == 1:
				odd = 1
			res += value // 2 * 2
		return res + 1 if odd else res


class Solution:
	def longestPalindrome(self, s: str) -> int:
		if len(s) == 1:
			return 1

		# count letters
		letters_dict = {}
		for l in s:
			letters_dict[l] = letters_dict[l] + 1 if letters_dict.get(l) else 1

		# Try to write the palindrome
		longest_palindrome = ''
		for key, value in sorted(letters_dict.items(), key=lambda x: x[1], reverse=True):
			while True:
				if value % 2 == 0 or \
						value % 3 == 0 or \
						value % 5 == 0 or \
						value % 7 == 0 or \
						value % 9 == 0:
					longest_palindrome += key * 2
					letters_dict[key] -= 2
					value -= 2

				elif value != 1:
					value -= 1

				if value <= 1:
					break

		total_len = len(longest_palindrome)
		if any(x for x in letters_dict.values()):
			total_len += 1

		return total_len


if __name__ == '__main__':
	S = Solution2()

	print('abccccdd -> 7: ', S.longestPalindrome('abccccdd'))
	print('a -> 1: ', S.longestPalindrome('a'))
	print('bb -> 2: ', S.longestPalindrome('bb'))
	print('aacbb -> 5: ', S.longestPalindrome('aacbb'))
	print('espaguethi -> 3: ', S.longestPalindrome('espaguethi'))
	print('ccc -> 3: ', S.longestPalindrome('ccc'))
	print('ababababa -> 11: ', S.longestPalindrome('"ababababa"'))
	print('aaabaaaa -> 7: ', S.longestPalindrome('aaabaaaa'))
	print('civilwartestin... -> 983: ', S.longestPalindrome('civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth'))
	print('jglknendpl... -> 445: ', S.longestPalindrome('jglknendplocymmvwtoxvebkekzfdhykknufqdkntnqvgfbahsljkobhbxkvyictzkqjqydczuxjkgecdyhixdttxfqmgksrkyvopwprsgoszftuhawflzjyuyrujrxluhzjvbflxgcovilthvuihzttzithnsqbdxtafxrfrblulsakrahulwthhbjcslceewxfxtavljpimaqqlcbrdgtgjryjytgxljxtravwdlnrrauxplempnbfeusgtqzjtzshwieutxdytlrrqvyemlyzolhbkzhyfyttevqnfvmpqjngcnazmaagwihxrhmcibyfkccyrqwnzlzqeuenhwlzhbxqxerfifzncimwqsfatudjihtumrtjtggzleovihifxufvwqeimbxvzlxwcsknksogsbwwdlwulnetdysvsfkonggeedtshxqkgbhoscjgpiel'))
