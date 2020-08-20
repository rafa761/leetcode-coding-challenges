"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:
Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""


# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


from copy import copy, deepcopy
from collections import OrderedDict


class Solution:
	def reorderList(self, head: ListNode) -> None:
		"""
		Do not return anything, modify head in-place instead.
		"""
		if not head:
			return []

		nodes_dict = OrderedDict()
		node = copy(head)
		idx = 1
		while node:
			nodes_dict[idx] = copy(node)
			nodes_dict[idx].next = None
			idx += 1
			node = node.next

		_, n = nodes_dict.popitem(last=False)
		head.val = n.val
		node = head
		while nodes_dict:
			_, n = nodes_dict.popitem(last=True)
			node.next.val = n.val
			node = node.next

			if not nodes_dict:
				break
			_, n = nodes_dict.popitem(last=False)
			node.next.val = n.val
			node = node.next


class Solution2:
	def reorderList(self, head: ListNode) -> None:
		"""
		Do not return anything, modify head in-place instead.
		"""
		if not head:
			return []

		slow, fast = head, head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next

		# reverse 2nd half of list
		prev = None
		curr = slow

		while curr:
			curr.next, prev, curr = prev, curr, curr.next

		# merge 2nd half with 1st half

		first, second = head, prev
		while second.next:
			tmp = first.next
			first.next = second
			first = tmp

			tmp = second.next
			second.next = first
			second = tmp




def print_linked_list(linked_list):
	node = linked_list
	while node:
		print(node.val, node.next)
		node = node.next


if __name__ == '__main__':
	S = Solution2()

	list1 = ListNode(1)
	list1.next = ListNode(2)
	list1.next.next = ListNode(3)
	list1.next.next.next = ListNode(4)

	S.reorderList(list1)
	print_linked_list(list1)

	list2 = ListNode(1)
	list2.next = ListNode(2)
	list2.next.next = ListNode(3)
	list2.next.next.next = ListNode(4)
	list2.next.next.next.next = ListNode(5)

	S.reorderList(list2)
	print_linked_list(list2)
