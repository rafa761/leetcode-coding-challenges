"""
5488. Minimum Operations to Make Array Equal

You have an array arr of length n where arr[i] = (2 * i) + 1 for all valid values of i (i.e. 0 <= i < n).

In one operation, you can select two indices x and y where 0 <= x, y < n and subtract 1 from arr[x] and add 1 to arr[y]
(i.e. perform arr[x] -=1 and arr[y] += 1). The goal is to make all the elements of the array equal.
It is guaranteed that all the elements of the array can be made equal using some operations.

Given an integer n, the length of the array. Return the minimum number of operations needed to make all the elements of arr equal.

Example 1:
Input: n = 3
Output: 2
Explanation: arr = [1, 3, 5]
First operation choose x = 2 and y = 0, this leads arr to be [2, 3, 4]
In the second operation choose x = 2 and y = 0 again, thus arr = [3, 3, 3].

Example 2:
Input: n = 6
Output: 9


Constraints:
1 <= n <= 10^4
"""
from collections import defaultdict


class Solution:
	def minOperations(self, n: int) -> int:
		arr = [2 * i + 1 for i in range(n)]

		target = sum(arr) // n
		res = 0
		for i in range(n // 2):
			res += target - arr[i]
		return res


if __name__ == '__main__':
	S = Solution()

	print('0 -> ', S.minOperations(1))
	print('1 -> ', S.minOperations(2))
	print('2 -> ', S.minOperations(3))
	print('4 -> ', S.minOperations(4))
	print('6 -> ', S.minOperations(5))
	print('9 -> ', S.minOperations(6))
	print('25 -> ', S.minOperations(10))
	print('17644200-> ', S.minOperations(8401))
