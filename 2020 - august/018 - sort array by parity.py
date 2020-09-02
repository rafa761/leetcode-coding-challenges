"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

Example 1:
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Note:
1 <= A.length <= 5000
0 <= A[i] <= 5000
"""
from typing import List


class Solution:
	def sortArrayByParity(self, A: List[int]) -> List[int]:
		even_list, odd_list = [], []
		for num in A:
			if num % 2 == 0:
				even_list.append(num)
			else:
				odd_list.append(num)

		return even_list + odd_list


class Solution2:
	def sortArrayByParity(self, A: List[int]) -> List[int]:
		# Base Case to stop recursion
		if len(A) <= 1:
			return A

		mid = len(A) // 2

		# Use recursion to create sub lists
		left_list, right_list = self.sortArrayByParity(A[:mid]), self.sortArrayByParity(A[mid:])

		return self.merge(left_list, right_list)

	def merge(self, left_list, right_list):
		result_list = []

		index_left = index_right = 0
		while index_left < len(left_list) and index_right < len(right_list):
			if self.is_even(left_list[index_left]):
				result_list.append(left_list[index_left])
				index_left += 1

			else:
				result_list.append(right_list[index_right])
				index_right += 1

		result_list.extend(left_list[index_left:])
		result_list.extend(right_list[index_right:])

		return result_list

	def is_even(self, number):
		return number % 2 == 0


class Solution3:
	def sortArrayByParity(self, A: List[int]) -> List[int]:
		A.sort(key=lambda x: x % 2)
		return A


if __name__ == '__main__':
	S = Solution3()

	print('[2,4,3,1] -> ', S.sortArrayByParity([3, 1, 2, 4]))
