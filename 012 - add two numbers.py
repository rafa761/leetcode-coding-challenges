"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		number_1 = []
		while hasattr(l1, 'val'):
			number_1.append(l1.val)
			l1 = l1.next
		n1 = ''.join([str(n) for n in number_1])[::-1]

		number_2 = []
		while hasattr(l2, 'val'):
			number_2.append(l2.val)
			l2 = l2.next
		n2 = ''.join([str(n) for n in number_2])[::-1]

		sum = int(n1) + int(n2)
		sum_list = [x for x in str(sum)[::-1]]

		root_node = ListNode(sum_list.pop(0))
		new_node = root_node
		while sum_list:
			new_node.next = ListNode(sum_list.pop(0))
			new_node = new_node.next

		return root_node


class Solution2:
	def addTwoNumbers(self, l1: ListNode, l2: ListNode, carry=0) -> ListNode:
		val = l1.val + l2.val + carry
		carry = val // 10
		ret = ListNode(val % 10)

		if (l1.next != None or l2.next != None or carry != 0):
			if l1.next == None:
				l1.next = ListNode(0)
			if l2.next == None:
				l2.next = ListNode(0)
			ret.next = self.addTwoNumbers(l1.next, l2.next, carry)
		return ret

class Solution3:
	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		result = ListNode(0)
		result_tail = result
		carry = 0

		while l1 or l2 or carry:
			val1 = l1.val if l1 else 0
			val2 = l2.val if l2 else 0
			carry, out = divmod(val1 + val2 + carry, 10)

			result_tail.next = ListNode(out)
			result_tail = result_tail.next

			l1 = l1.next if l1 else None
			l2 = l2.next if l2 else None

		return result.next



if __name__ == '__main__':
	S = Solution3()
	L1 = ListNode(2)
	L1.next = ListNode(4)
	L1.next.next = ListNode(3)

	L2 = ListNode(5)
	L2.next = ListNode(6)
	L2.next.next = ListNode(4)

	print('7 -> 0 -> 8: ', S.addTwoNumbers(L1, L2))

	test = S.addTwoNumbers(L1, L2)

	while hasattr(test, 'val'):
		print('val: ', test.val, 'next: ', test.next)
		test = test.next
