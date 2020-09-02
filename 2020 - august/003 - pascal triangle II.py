"""Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
# 3 -> [1,3,3,1]

Follow up: Could you optimize your algorithm to use only O(k) extra space?
"""
from typing import List


class Solution:
	def getRow(self, rowIndex: int) -> List[int]:
		return self.__get_pyramid(rowIndex)

	def __get_pyramid(self, rowIndex, current_index=None, current_row=None):
		if not rowIndex:
			return [1]

		if current_index is not None:
			if current_index > rowIndex:
				return current_row

		if not current_row:
			return self.__get_pyramid(rowIndex, 0, [1])

		if len(current_row) == 1:
			return self.__get_pyramid(rowIndex, 1, [1, 1])

		current_list = []
		for i in range(current_index + 1):
			if i == 0 or i == current_index:
				current_list.append(1)
			else:
				current_list.append(current_row[i-1] + current_row[i])

		return self.__get_pyramid(rowIndex, current_index + 1, current_list)





if __name__ == '__main__':
	S = Solution()

	print('0 -> [1]:', S.getRow(0))
	print('3 -> [1, 3, 3, 1]:', S.getRow(3))
	print('4 -> [1, 4, 6, 4, 1]:', S.getRow(4))
	print('5 -> [1, 5, 10, 10, 5, 1]:', S.getRow(5))
