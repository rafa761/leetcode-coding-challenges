"""
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had
             received 3, 0, 6, 1, 5 citations respectively.
             Since the researcher has 3 papers with at least 3 citations each and the remaining
             two with no more than 3 citations each, her h-index is 3.
Note: If there are several possible values for h, the maximum one is taken as the h-index.
An easy approach is to sort the array first.
What are the possible values of h-index?
A faster approach is to use extra space.
"""
from typing import List


class Solution:
	def hIndex(self, citations: List[int]) -> int:
		if not citations:
			return 0

		citations.sort()
		length = len(citations)
		h_index = 0
		for i in range(length):
			idx = length - i
			if citations[i] >= idx and (i < 1 or citations[i - 1] <= idx):
				h_index = max(h_index, idx)

		return h_index


if __name__ == '__main__':
	S = Solution()

	print('[3, 0, 6, 1, 5] -> 3: ', S.hIndex([3, 0, 6, 1, 5]))
	print('[9, 0, 6, 1, 5, 4, 7] -> 4: ', S.hIndex([9, 0, 6, 1, 5, 4, 7]))
	print('[1, 5, 8, 8, 6, 3, 7, 4] -> 5: ', S.hIndex([1, 5, 8, 8, 6, 3, 7, 4]))
	print('[0, 3, 4, 7, 8, 9, 10, 11] -> 5: ', S.hIndex([0, 3, 4, 7, 8, 9, 10, 11]))
	print('[0] -> 0: ', S.hIndex([0]))
	print('[1] -> 1: ', S.hIndex([1]))
	print('[100] -> 1: ', S.hIndex([100]))
	print('[11,15] -> 2: ', S.hIndex([11, 15]))
