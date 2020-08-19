"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
"""
from typing import List
from itertools import chain


class Solution:
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		complete_list = nums1.copy()
		complete_list.extend(nums2)
		complete_list.sort()

		quotient, remainder = divmod(len(complete_list), 2)
		if remainder:
			return complete_list[quotient]
		return float(sum(complete_list[quotient - 1:quotient + 1]) / 2)


class Solution2:
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		complete_list = nums1 + nums2
		complete_list.sort()

		len_list = len(complete_list)

		result = complete_list[len_list // 2]
		if len_list % 2 == 0:
			a = complete_list[len_list // 2 - 1]
			b = complete_list[len_list // 2]
			result = (a + b) / 2

		return result


if __name__ == '__main__':
	S = Solution2()

	print('2.0 -> ', S.findMedianSortedArrays([1, 3], [2]))
	print('2.5 -> ', S.findMedianSortedArrays([1, 2], [3, 4]))
