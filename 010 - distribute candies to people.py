"""
We distribute some number of candies, to a row of n = num_people people in the following way:

We then give 1 candy to the first person, 2 candies to the second person, and so on until we give n candies
 to the last person.

Then, we go back to the start of the row, giving n + 1 candies to the first person, n + 2 candies to the second person,
and so on until we give 2 * n candies to the last person.

This process repeats (with us giving one more candy each time, and moving to the start of the row after we
 reach the end) until we run out of candies.  The last person will receive all of our remaining
  candies (not necessarily one more than the previous gift).

Return an array (of length num_people and sum candies) that represents the final distribution of candies.


Example 1:
Input: candies = 7, num_people = 4
Output: [1,2,3,1]
Explanation:
On the first turn, ans[0] += 1, and the array is [1,0,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0,0].
On the third turn, ans[2] += 3, and the array is [1,2,3,0].
On the fourth turn, ans[3] += 1 (because there is only one candy left), and the final array is [1,2,3,1].

Example 2:
Input: candies = 10, num_people = 3
Output: [5,2,3]
Explanation:
On the first turn, ans[0] += 1, and the array is [1,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0].
On the third turn, ans[2] += 3, and the array is [1,2,3].
On the fourth turn, ans[0] += 4, and the final array is [5,2,3].


Constraints:
1 <= candies <= 10^9
1 <= num_people <= 1000

Hint:
Give candy to everyone each "turn" first [until you can't], then give candy to one person per turn.
"""
from typing import List


class Solution:
	def distributeCandies(self, candies: int, num_people: int) -> List[int]:
		people_dict = {i: 0 for i in range(num_people)}

		current_count = 1
		while candies > 0:
			for i in range(num_people):
				if current_count <= candies:
					people_dict[i] = people_dict[i] + current_count
					candies -= current_count

				else:
					people_dict[i] = people_dict[i] + candies
					candies = 0

				current_count += 1

		return [x for x in people_dict.values()]


class Solution2:
	def distributeCandies(self, candies: int, num_people: int) -> List[int]:
		whole_row: int = (1 + num_people) * num_people // 2
		inc: int = num_people * num_people
		rows: int = 0

		while candies >= whole_row:
			rows += 1
			candies -= whole_row
			whole_row += inc

		base: int = rows + rows * (rows - 1) * num_people // 2
		given: List[int] = (
			[0] * num_people if base == 0 else
			[(base + rows * i) for i in range(num_people)]
		)

		i: int = 0
		to_give: int = num_people * rows + 1
		while candies >= to_give:
			candies -= to_give
			given[i] += to_give
			i, to_give = i + 1, to_give + 1

		given[i] += candies
		return given

class Solution3:
	def distributeCandies(self, candies: int, num_people: int) -> List[int]:
		candies_list = [0] * num_people

		count = 0
		while candies > 0:
			for i in range(num_people):
				count = count + 1

				if count <= candies:
					candies = candies - count
					candies_list[i] = candies_list[i] + count

				else:
					candies_list[i] = candies_list[i] + candies
					candies = 0
		return candies_list




if __name__ == '__main__':
	S = Solution3()

	print('[1,2,3,1] -> ', S.distributeCandies(7, 4))
	print('[5,2,3] -> ', S.distributeCandies(10, 3))
	print('[1,2,1,0,0] -> ', S.distributeCandies(4, 5))
	print('[1] -> ', S.distributeCandies(1, 1))
	print('[6] -> ', S.distributeCandies(6, 1))
	print('[1,1,0,0,0,0,0,0] -> ', S.distributeCandies(2, 8))
