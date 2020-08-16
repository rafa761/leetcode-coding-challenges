"""
5185. Three Consecutive Odds

Given an integer array arr, return true if there are three consecutive odd numbers in the array.
Otherwise, return false.

Example 1:
Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.

Example 2:
Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.

Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
"""
from typing import List


class Solution:
	def threeConsecutiveOdds(self, arr: List[int]) -> bool:
		def is_odd(n):
			return n % 2 != 0

		count_odd = 0
		for num in arr:
			if is_odd(num):
				count_odd += 1
			else:
				count_odd = 0

			if count_odd == 3:
				return True

		return False


if __name__ == '__main__':
	S = Solution()

	print('False -> ', S.threeConsecutiveOdds([2, 6, 4, 1]))
	print('True -> ', S.threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12]))
	print('False -> ', S.threeConsecutiveOdds([]))
	print('True -> ', S.threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 24, 12, 18, 24, 12, 18, 24, 12, 18, 24, 12, 18, 24, 12, 18, 24, 12, 18, 24, 12, 18, 24, 12, 18, 24, 12, 18, 24, 12, 18, 24, 12, 18, 24, 12, 18, 24, 12, 18, 24, 12, 18, 24, 12, 18, 24, 12, 18, 24, 12, 18, 24, 12, 18, 24, 12, 18, 24, 12, 18, 24, 12, 18, 24, 12, 18, 24, 12, 18, 24, 12, 18, 24, 12, 18, 24, 12, 18, 24, 12, 18, 24, 12, 18, 24, 12, 18, 24, 12, 18, 24, 12, 18, 24, 12, 18, 24, 12, 18, 24, 12, 18, 99, 103, 257]))
