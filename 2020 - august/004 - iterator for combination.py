"""
Design an Iterator

class , which has:

A constructor that takes a string characters of sorted distinct lowercase English letters and a number
combinationLength as arguments.

A function next() that returns the next combination of length combinationLength in lexicographical order.

A function hasNext() that returns True if and only if there exists a next combination.

Example:

CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false

Constraints:

1 <= combinationLength <= characters.length <= 15
There; will; be; at; most; 10 ^ 4; function; calls; per; test.;
It's guaranteed that all calls of the function next are valid.

Generate all combinations as a processing
use bit masking to generate all the combinations
"""
from itertools import combinations

class CombinationIterator:
	def __init__(self, characters: str, combinationLength: int):
		self.actual_index = 0
		self.combinations_list = []
		for char in combinations(characters, combinationLength):
			self.combinations_list.append(''.join(char))

	def next(self):
		next = self.combinations_list[self.actual_index]
		self.actual_index += 1
		return next

	def hasNext(self):
		return self.actual_index < len(self.combinations_list)


if __name__ == '__main__':
	C = CombinationIterator('abc', 2)

	print('abc - next -> ab: ', C.next())
	print('abc - hasNext -> true: ', C.hasNext())
	print('abc - next -> ac: ', C.next())
	print('abc - hasNext -> true: ', C.hasNext())
	print('abc - next -> bc: ', C.next())
	print('abc - hasNext -> false: ', C.hasNext())

	print('------------------------------------')
	C = CombinationIterator('abcd', 3)

	print('abcd - next -> abc: ', C.next())
	print('abcd - hasNext -> true: ', C.hasNext())
	print('abcd - next -> abd: ', C.next())
	print('abcd - hasNext -> true: ', C.hasNext())
	print('abcd - next -> acd: ', C.next())
	print('abcd - hasNext -> true: ', C.hasNext())
	print('abcd - next -> bcd: ', C.next())
	print('abcd - hasNext -> false: ', C.hasNext())
